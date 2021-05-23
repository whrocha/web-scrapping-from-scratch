STACK_NAME=web-scrapping-test

AWS_PROFILE=default
AWS_REGION=us-east-1

ARTIFACT_STORE_BUCKET_NAME=$$(aws cloudformation describe-stacks \
	 --profile=$(AWS_PROFILE) \
	 --region=$(AWS_REGION) \
	 --stack-name=${STACK_NAME} \
	 --query="Stacks[].Outputs[?OutputKey == 'ArtifactStoreBucket'].OutputValue" \
	 --output text)

deploy:
	sam build
	sam deploy \
		--profile=$(AWS_PROFILE) \
		--region=$(AWS_REGION) \
		--stack-name=$(STACK_NAME) \
		--capabilities CAPABILITY_AUTO_EXPAND CAPABILITY_IAM \
		--no-fail-on-empty-changeset \ 
		--s3-bucket=$(ARTIFACT_STORE_BUCKET_NAME) \
		--s3-prefix=cf-packages/$(STACK_NAME) \
		--force-upload