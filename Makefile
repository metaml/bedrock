.DEFAULT_GOAL = help

#export ACCOUNT_ID = 975050288432
export SHELL=bash
export AWS_DEFAULT_REGION = us-east-1

aws-id: ## aws identity
	aws sts get-caller-identity

# impure needed to read the above env var
dev: ## nix develop
	nix develop

MODELID   = meta.llama3-2-1b-instruct-v1:0    # foundational model
MODELIDIP = us.$(MODELID) # inference profile

llama: ## converse
	source .env \
	&& ./llama.py

invoke-model: ## invoke-model
	source .env \
	&& aws bedrock-runtime invoke-model \
		--model-id $(MODELIDIP) \
		--body '{"prompt": "formatted_prompt", "max_gen_len": 512, "temperature": 0.5 }' \
		--cli-binary-format raw-in-base64-out \
		--output json \
		invoke-model.json

help: ## help
	@grep -E '^[a-zA-Z00-9_%-]+:.*?## .*$$' $(MAKEFILE_LIST) \
	| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-18s\033[0m %s\n", $$1, $$2}'

clean: ## clean
	find . -name \*~ | xargs rm -f
	rm -f *.json *.txt

clobber: clean ## clobber dev env
	rm -rf venv/*

login-aws: ## login to aws to fetch/refresh token
	PYTHONPATH= aws sso login # AdministratorAccess-975050288432
