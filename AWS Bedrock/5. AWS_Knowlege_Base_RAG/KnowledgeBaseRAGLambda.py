import json
import boto3

client_bedrock_knowledgebase = boto3.client('bedrock-agent-runtime')

def lambda_handler(event, context):
    user_prompt = event['prompt']
    client_knowledgebase = client_bedrock_knowledgebase.retrieve_and_generate(
        input={
            'text': user_prompt
        },
        retrieveAndGenerateConfiguration={
            'type': 'KNOWLEDGE_BASE',
            'knowledgeBaseConfiguration' : {
                'knowledgeBaseId' : 'w234e',
                'modelArn' : 'arn:aws:bedrock:us-east-1:166007334679:inference-profile/us.anthropic.claude-3-5-haiku-20241022-v1:0'
            }
        }
    )
    response_final = client_knowledgebase['output']['text']
    return {
        'statusCode': 200,
        'body': json.dumps(response_final)
    }
