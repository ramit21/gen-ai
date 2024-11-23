import json

def lambda_handler(event, context):
    #follow this for request/response formats: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-lambda.html
    agent = event['agent']
    print('Event sent from agent - ' + agent +' is ' + event)
    reportId = event['parameters'][0]['value']
    responseObj = {
        'reportId' : reportId,
        'status': 'Pending',
        'diagnosis': ''
    }
    if(reportId == '1234'):
        responseObj['status'] = 'Available'
        responseObj['diagnosis'] = 'Blastocystis Hominis'
    print('Response object = ' + responseObj)
    
    #prepare response as per above url
    response_body = {
        'application/json': {
            'body': json.dumps(responseObj)
        }
    }
    action_response = {
        'actionGroup': event['actionGroup'],
        'apiPath': event['apiPath'],
        'httpMethod': event['httpMethod'],
        'httpStatusCode': 200,
        'responseBody': response_body
    }
    session_attributes = event['sessionAttributes']
    prompt_session_attributes = event['promptSessionAttributes']
    api_response = {
        'messageVersion': '1.0', 
        'response': action_response,
        'sessionAttributes': session_attributes,
        'promptSessionAttributes': prompt_session_attributes
    }
    return api_response