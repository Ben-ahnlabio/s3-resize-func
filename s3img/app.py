import pathlib
import tempfile
import boto3
import uuid
from urllib.parse import unquote_plus
from s3img import imgtool

s3_client = boto3.client("s3")


def lambda_handler(event, context):
    heights = [250, 500, 750, 1000]
    for record in event["Records"]:
        bucket = record["s3"]["bucket"]["name"]
        key = unquote_plus(record["s3"]["object"]["key"])
        tmpkey = key.replace("/", "")
        download_path = "/tmp/{}{}".format(uuid.uuid4(), tmpkey)
        s3_client.download_file(bucket, key, download_path)
        with tempfile.TemporaryDirectory() as dir:
            images = imgtool.make_thumbnails(
                pathlib.Path(download_path), heights, pathlib.Path(dir)
            )
            for img_path in images:
                s3_client.upload_file(str(img_path), "{}-resized".format(bucket), key)
