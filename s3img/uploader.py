import os
import pathlib
import boto3
import mypy_boto3_s3


def s3_client():
    return boto3.client(
        service_name="s3",
        region_name=os.getenv("AWS_S3_REGION_NAME"),
        aws_access_key_id=os.getenv("AWS_S3_ACCESS_KEY"),
        aws_secret_access_key=os.getenv("AWS_S3_SECRET_KEY"),
    )


def upload_file(
    s3_client: mypy_boto3_s3.S3Client, filepath: pathlib.Path, s3_name: str
):
    bucket_name = os.getenv("AWS_S3_BUCKET_NAME")
    if bucket_name:
        return s3_client.upload_file(
            str(filepath),
            bucket_name,
            s3_name,
        )
        # return s3_client.upload_file(str(filepath), bucket_name, s3_name, ExtraArgs={'ContentType': "application/json", 'ACL': "public-read"})
    else:
        raise ValueError("AWS_S3_BUCKET_NAME")
