.PHONY: core_build

STACK_NAME=web-scrapping-test

AWS_PROFILE=default
AWS_REGION=us-east-1

ARTIFACT_STORE_BUCKET_NAME=$$(aws cloudformation describe-stacks \
	 --profile=$(AWS_PROFILE) \
	 --region=$(AWS_REGION) \
	 --stack-name=core-build \
	 --query="Stacks[].Outputs[?OutputKey == 'ArtifactStoreBucket'].OutputValue" \
	 --output text)

deploy: core_build
	sam build
	sam deploy \
		--profile=$(AWS_PROFILE) \
		--region=$(AWS_REGION) \
		--stack-name=$(STACK_NAME) \
		--capabilities CAPABILITY_AUTO_EXPAND CAPABILITY_IAM \
		--no-fail-on-empty-changeset \
		--s3-prefix=cf-packages/$(STACK_NAME) \
		--force-upload \
		--s3-bucket=$(ARTIFACT_STORE_BUCKET_NAME)

core_build: core_build.yaml
	aws cloudformation deploy \
		--profile=$(AWS_PROFILE) \
		--region=$(AWS_REGION) \
		--capabilities=CAPABILITY_IAM \
		--no-fail-on-empty-changeset \
		--stack-name=core-build \
		--template-file=$<