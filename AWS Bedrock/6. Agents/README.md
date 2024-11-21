# Bedrock Agents

Amazon Bedrock Agents are designed to streamline workflows and automate repetitive tasks by leveraging generative AI.

First you provide a openapi spec Swagger documentation (via a S3 bucket) to the Agent.
API endpoints in this swagger will point to names of Lambda functions.
When user gives a prompt to the Agent, it will try to match it to a Lambda based on the 
'description' field given in swagger spec.
From Lambda you can then invoke other AWS databases like Daynamodb, Auora etc to fetch data as per the lambda use case.
Response of Lambda has to follow format expected from Bedrock Agent.

You also select the FM to use with the Agent.

You can additionally provide a Knowledge Base to the Agent, which will serve the purpose of RAG store. So if user's prompt is not matched against API spec, it will try to find something in the RAG store, and then return the response as per the RAG context and the FM selected for use.
At time of creating the Agent, you can give it instructions like 'Act like xyz and give your responses in abc format.'

Agents work on 'Chain of thought' process.


## POC Setup
Steps taken along with screenshots for running this POC:
1. 
2. 
