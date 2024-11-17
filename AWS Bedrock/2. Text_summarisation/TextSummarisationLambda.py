import json
import boto3
import base64
import datetime
#Create client connection with Bedrock and S3
client_s3 = boto3.client('s3')
client_bedrock = boto3.client('bedrock-runtime')


def lambda_handler(event, context):
    input_prompt = event['prompt']
    requestbody = json.dumps({
        "prompt": input_prompt,
        "temperature": 0.9,
        "p": 0.75,
        "k": 0,
        "max_tokens": 100
    })
    response_bedrock = client_bedrock.invoke_model(
        contentType = 'application/json',
        accept = 'application/json',
        modelId = 'cohere.command-text-v14', 
        body = requestbody
    )
    response_bedrock_string = json.loads(response_bedrock['body'].read())
    response_final = response_bedrock_string['generations'][0]['text']
    return {
        'statusCode': 200,
        'body': json.dumps(response_final)
    }
