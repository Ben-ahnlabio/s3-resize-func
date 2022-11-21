from s3img import uploader


def test_s3_client(s3_env):
    s3_client = uploader.s3_client()
    assert s3_client
