import logging
import mimetypes
import pathlib
import tempfile
from urllib.parse import unquote_plus

import boto3
import imgtool

s3_client = boto3.client("s3")

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


def lambda_handler(event, context):
    heights = [250, 500, 750, 1000]
    for record in event["Records"]:
        bucket = record["s3"]["bucket"]["name"]
        key = unquote_plus(record["s3"]["object"]["key"])
        tmpkey = key.replace("/", "")
        download_path = "/tmp/{}".format(tmpkey)
        s3_client.download_file(bucket, key, download_path)

        mimetypes.add_type("image/webp", ".webp")
        mime_type, _ = mimetypes.guess_type(download_path)
        # mime_type = magic.from_file(download_path, mime=True)
        if mime_type is None or not mime_type.startswith("image/"):
            log.info("mimetype=%s. skip.", mime_type)
            return

        # 원본 resized bucket 에 복사
        s3_client.upload_file(
            Filename=download_path,
            Bucket="{}-resized".format(bucket),
            Key=pathlib.Path(download_path).name,
            ExtraArgs={"ContentType": mime_type},
        )

        with tempfile.TemporaryDirectory() as dir:
            images = imgtool.make_thumbnails(
                pathlib.Path(download_path), heights, pathlib.Path(dir)
            )
            for img_path in images:
                s3_client.upload_file(
                    Filename=str(img_path),
                    Bucket="{}-resized".format(bucket),
                    Key=img_path.name,
                    ExtraArgs={"ContentType": mime_type},
                )
