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
        "text_prompts": [
        {
        "text": input_prompt
        }
    ],
    "cfg_scale": 10,
    "seed": 10, # seed 0 would mean generate same image every time
    "steps": 30
    })
    response_bedrock = client_bedrock.invoke_model(
        contentType = 'application/json',
        accept = 'application/json',
        modelId = 'stability.stable-diffusion-xl-v1', 
        body = requestbody
    )  
    # as per model documentation, data resides as StreamingBody() against body
    # convert StreamingBody to bytes using json_loads
    response_bedrock_bytes = json.loads(response_bedrock['body'].read())
    # now further extract image data from artifact key and base64 decode
    response_bedrock_base64 = response_bedrock_bytes['artifacts'][0]['base64']
    response_bedrock_finalimage = base64.b64decode(response_bedrock_base64)
    # store the image in S3 with a key
    pic_key = 'picKey' + datetime.datetime.today().strftime('%Y-%M-%D-%M-%S')
    client_s3.put_object(
        Bucket = 'genai-image-17-11-24', # update with your bucket name
        Body = response_bedrock_finalimage,
        Key = pic_key
    )
    #generate presignd url
    response = client_s3.generate_presigned_url('get_object',
                                                Params={'Bucket': 'genai-image-17-11-24',
                                                        'Key': pic_key},
                                                ExpiresIn=3600)
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
