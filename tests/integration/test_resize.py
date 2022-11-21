import pathlib
from s3img import imgtool


def test_make_thumbnails_png():
    img_filepath = pathlib.Path(".data/nft_original.png")
    result = imgtool.make_thumbnails(
        img_filepath, [250, 500, 750, 1000], pathlib.Path("/mnt/c/Users/ben/Downloads")
    )
    assert result


def test_make_thumbnails_gif():
    img_filepath = pathlib.Path(".data/nft_original.gif")
    result = imgtool.make_thumbnails(
        img_filepath, [250, 500, 750, 1000], pathlib.Path("/mnt/c/Users/ben/Downloads")
    )
    assert result


def test_make_thumbnails_webp():
    img_filepath = pathlib.Path(".data/nft_original.webp")
    result = imgtool.make_thumbnails(
        img_filepath, [250, 500, 750, 1000], pathlib.Path("/mnt/c/Users/ben/Downloads")
    )
    assert result


def test_resize_gif():
    img_filepath = pathlib.Path(".data/nft_original.gif")
    imgtool.resize_image(
        img_filepath,
        250,
        pathlib.Path("/mnt/c/Users/ben/Downloads/nft_original_h250.gif"),
    )
    imgtool.resize_image(
        img_filepath,
        500,
        pathlib.Path("/mnt/c/Users/ben/Downloads/nft_original_h500.gif"),
    )
    imgtool.resize_image(
        img_filepath,
        750,
        pathlib.Path("/mnt/c/Users/ben/Downloads/nft_original_h750.gif"),
    )
    imgtool.resize_image(
        img_filepath,
        1000,
        pathlib.Path("/mnt/c/Users/ben/Downloads/nft_original_h1000.gif"),
    )


def test_resize_png():
    img_filepath = pathlib.Path(".data/nft_original.png")
    imgtool.resize_image(
        img_filepath,
        250,
        pathlib.Path("/mnt/c/Users/ben/Downloads/nft_original_h250.png"),
    )
    imgtool.resize_image(
        img_filepath,
        500,
        pathlib.Path("/mnt/c/Users/ben/Downloads/nft_original_h500.png"),
    )
    imgtool.resize_image(
        img_filepath,
        750,
        pathlib.Path("/mnt/c/Users/ben/Downloads/nft_original_h750.png"),
    )
    imgtool.resize_image(
        img_filepath,
        1000,
        pathlib.Path("/mnt/c/Users/ben/Downloads/nft_original_h1000.png"),
    )


def test_resize_jpg():
    img_filepath = pathlib.Path(".data/nft_original.jpg")
    imgtool.resize_image(
        img_filepath,
        250,
        pathlib.Path("/mnt/c/Users/ben/Downloads/nft_original_h250.jpg"),
    )
    imgtool.resize_image(
        img_filepath,
        500,
        pathlib.Path("/mnt/c/Users/ben/Downloads/nft_original_h500.jpg"),
    )
    imgtool.resize_image(
        img_filepath,
        750,
        pathlib.Path("/mnt/c/Users/ben/Downloads/nft_original_h750.jpg"),
    )
    imgtool.resize_image(
        img_filepath,
        1000,
        pathlib.Path("/mnt/c/Users/ben/Downloads/nft_original_h1000.jpg"),
    )


def test_resize_webp():
    img_filepath = pathlib.Path(".data/nft_original.webp")
    imgtool.resize_image(
        img_filepath,
        250,
        pathlib.Path("/mnt/c/Users/ben/Downloads/nft_original_h250.webp"),
    )
    imgtool.resize_image(
        img_filepath,
        500,
        pathlib.Path("/mnt/c/Users/ben/Downloads/nft_original_h500.webp"),
    )
    imgtool.resize_image(
        img_filepath,
        750,
        pathlib.Path("/mnt/c/Users/ben/Downloads/nft_original_h750.webp"),
    )
    imgtool.resize_image(
        img_filepath,
        1000,
        pathlib.Path("/mnt/c/Users/ben/Downloads/nft_original_h1000.webp"),
    )
