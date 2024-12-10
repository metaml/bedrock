#### AWS Bedrock "Hello, World!"

* .env
  * create a ".env" file

```
export AWS_ACCESS_KEY_ID=...
export AWS_SECRET_ACCESS_KEY=...
export AWS_DEFAULT_REGION=us-east-1
```

* Makefile
  * make help
    * shows all the targets
  * make converse
    * sources .env
    * executes converse.py
