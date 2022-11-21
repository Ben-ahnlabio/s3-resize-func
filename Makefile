init:
	poetry export --without-hashes --format=requirements.txt > s3img/requirements.txt
	sam build --use-container --build-image ResizeFunction=amazon/aws-sam-cli-build-image-python3.8
