import pathlib
import shutil
from typing import List
from PIL import ImageFile, Image, ImageSequence

ImageFile.LOAD_TRUNCATED_IMAGES = True


def make_thumbnails(
    image_filepath: pathlib.Path, heights: List[int], output_dir: pathlib.Path
):
    """image 의 높이가 heights 인 resize image 를 생성함.
    heights list length 만큼 이미지를 생성함.
    원본 이미지의 비율을 깨뜨리지 않고 유지함.
    resize 이후에도 file format 을 유지함.
    생성될 이미지가 원본 이미지보다 큰 경우는 생성하지 않고 파일을 복사함.

    원본 파일의 이름 뒤에 h{size} 를 붙여 구분.

    예를들어 원본 이미지 파일이름이 'abc.png' 일때 heights 인자에 [100,200,300] 값을 입력하면 아래 3개의 파일이 생성됨.
    - abc_h100.png
    - abc_h200.png
    - abc_h300.png

    Args:
        image_filepath: 이미지파일 경로
        heights: 조정될 높이값 list
        output_dir: 새로 생성된 파일이 저장될 경로

    Returns:
        pathlib.Path list. 새로 생성된 파일의 경로 list.
    """

    def _resize_image(img, height, resize_func):
        """원본 이미지의 높이가 새로 생성될 이미지보다 큰 경우에만 resize
        그렇지 않으면 파일을 복사함"""
        of = pathlib.Path(
            output_dir / f"{image_filepath.stem}_h{height}{image_filepath.suffix}"
        )
        if height < img.height:
            resize_func(img, height, of)
        else:
            shutil.copy(image_filepath, of)
        return of

    img = Image.open(image_filepath)
    if img.format == "GIF" or img.format == "WEBP":
        return [_resize_image(img, h, resize_animation) for h in heights]
    else:
        return [_resize_image(img, h, resize_img) for h in heights]


def resize_image(
    image_filepath: pathlib.Path, height: int, output_filepath: pathlib.Path
) -> pathlib.Path:
    img = Image.open(image_filepath)
    if img.format == "GIF" or img.format == "WEBP":
        resize_animation(img, height, output_filepath)
    else:
        resize_img(img, height, output_filepath)

    return output_filepath


def resize_img(image, height, target_filepath):
    ratio = height / image.height
    img_resize = image.resize(
        (int(image.width * ratio), int(image.height * ratio)), Image.LANCZOS
    )
    img_resize.save(target_filepath, image.format, quality=95)


def resize_animation(image, height, target_filepath):
    ratio = height / image.height
    size = int(image.width * ratio), int(image.height * ratio)
    frames = ImageSequence.Iterator(image)

    def thumbnails(frames):
        # https://pillow.readthedocs.io/en/stable/handbook/concepts.html#PIL.Image.NEAREST
        for frame in frames:
            thumbnail = frame.copy()
            # thumbnail.thumbnail(size, Image.LANCZOS) # best quality
            thumbnail.thumbnail(size, Image.NEAREST)  # low quality, high performance
            yield thumbnail

    frames = thumbnails(frames)

    # Save output
    om = next(frames)  # Handle first frame separately
    om.info = image.info  # Copy sequence info
    om.save(target_filepath, save_all=True, append_images=list(frames), quality=20)
