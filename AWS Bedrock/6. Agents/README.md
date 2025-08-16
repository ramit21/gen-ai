# Bedrock Agents

Amazon Bedrock Agents are designed to streamline workflows and automate repetitive tasks by leveraging generative AI.

First you provide a openapi spec Swagger documentation (via a S3 bucket) to the Agent.
API endpoints in this swagger will point to names of Lambda functions.
When user gives a prompt to the Agent, it will try to match it to a Lambda based on the 
'description' field given in swagger spec.
From Lambda you can then take actions like invoking other AWS databases like Daynamodb, Auora etc to fetch data as per the use case.
Response of Lambda has to follow format expected from Bedrock Agent spec.

You also select the FM to use with the Agent.

You can additionally provide a Knowledge Base to the Agent, which will serve the purpose of RAG store. So if user's prompt is not matched against API spec, it will try to find something in the RAG store, and then return the response as per the RAG context and the FM selected for use.

At time of creating the Agent, you can give it instructions like 'Act like xyz and give your responses in abc format.'

See the attached architecture screenshot on how the Agent works.

Agents work on 'Chain of thought' process. It processes input to repsonse in 3 steps:
1. **Pre-processing**: Agent processes user input prompt and enriches it with its own prompt store database making it more conducive for the foundation model selected. It also checks if the prompt is malicious and if its in the domain of the agent. Eg. An agent instructed to act like as health report expert, will say no to any question asked about banking or finance.
2. **Orchestration**: In this step, the selected foundation model looks at user input, swagger api mapping, and instruction provided to the agent (act as ...), breaks down the task into manageable steps (chain of thought) on how to execute the task - eg. it will first try to map prompt to a swagger api descriptin, if not found then it goes to Knowledge Base etc.
3. **Post-processing**: Steps taken to generate a final response from invoking action groups, knowledge bases, and model outputs.

When you test the Agent, you can see the trace of actions taken for each of the above steps. (see screenshot as eg.) 

## POC Setup
Steps taken along with screenshots for running this POC:
1. Create Swagger api which point description to respective lambda function. You can view and validate swagger spec at https://editor.swagger.io/
2. Upload the same in S3 bucket.
3. Create Lambda function (code attached), which in our POC returns hardcoded response, but in real world can also be fetching details from downstreams databases.
4. Ensure that request/response of Lambda function follows Bedrock Agent spec, as it will be the Agent that will be invoking this lambda and processing the response. Follow this documentation for the same: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-lambda.html
5. Create Agent. Take care of below when creating the Agent:
```
Select the FM eg. Anthropic Claude.
Add instruction: 'You are an assistant chatbot in health care. You are friendly and polite. You resolve customer queries by providing health reports with the status. Refuse to answer any other topic than health-related.'
Add Action Group to point to S3 bucket with swagger and select lambda function name (refer screenshot).
```
6. Since Agent is supposed to call the Lambda function, add resource based permission to Lambda. Go to Lambda -> Configuration -> Permissions -> scroll down to 'Resource based policy statements -> Add Permissions -> Select AWS Service -> Other (as Bedrock not available in dropdown yet)-> enter below values for:
```
Principal : bedrock.amazonaws.com
Source ARN: ARN of the Agent
Action: lambda:InvokeFunction
```
7. Next, upload your knowledge base PDFs in a S3 bucket and create a Bedrock Knowledge from it. Sample PDF with more details of a particular disease are attached.
8. Update the agent and set the knowledge base created above. It is very important that you also enter the instruction which will decide when Agent will invoke the knowledge base. For this POC, below text was used:
```
Bedrock Agent will utlise the knowledge base to answer any questions about diagnosis mentioned in the report statuses.
```
10. While not covered in this POC, you can create an API gateway that would invoke Agent directly as RESTful resources.
11. Test the agent giving it prompts that would invoke Lambda, and prompts that would fetch response from RAG store instead. As attached screenshots, one can see responses to following questions:
 
 A question on embedded finance is refused by the agent as it has been instructed to only answer health related queries.

 A question of status of report id 999 is returned form lambda as 'Pending'.

 A question on report id 1234 - returns status as 'Available' and diagnosis as 'Blastocystis Hominis' from Lambda, and then includes indormation on the diagnosis from Knowledge Store RAG.
