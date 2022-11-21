init:
	poetry export --without-hashes --format=requirements.txt > requirements.txt
	sam build --use-container --build-image Function1=amazon/aws-sam-cli-build-image-python3.8