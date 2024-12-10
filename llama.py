#!/usr/bin/env python3

from botocore.exceptions import ClientError
import boto3
import json

client = boto3.client("bedrock-runtime", region_name="us-east-1")
model_id = "us.meta.llama3-1-70b-instruct-v1:0"
prompt = "Hello, who won the 2022 World Cup?"

# embed the prompt in Llama 3's instruction format.
formatted_prompt = f"""
<|begin_of_text|><|start_header_id|>user<|end_header_id|>
{prompt}
<|eot_id|>
<|start_header_id|>assistant<|end_header_id|>
"""
native_request = {
  "prompt": formatted_prompt,
  "max_gen_len": 512,
  "temperature": 0.5,
}

req = json.dumps(native_request)

try:
    res = client.invoke_model(modelId=model_id, body=req)
except (ClientError, Exception) as e:
    print(f"error: can't invoke '{model_id}'; exception: {e}")
    exit(1)

# decode the response body.
response = json.loads(res["body"].read())
print(f"response: \n{response}")

generation = response["generation"]
print(f"generation: \n{generation}")
