import dotenv
import pathlib
import tempfile
import pytest


@pytest.fixture
def random_file():
    with tempfile.TemporaryDirectory() as dir:
        tmpfile = pathlib.Path(dir) / "filename"
        with tmpfile.open("w") as f:
            f.write("file .. ")
        yield tmpfile


@pytest.fixture
def s3_env():
    dotenv.load_dotenv()
