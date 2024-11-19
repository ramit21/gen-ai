# Bedrock Knowledge Base

In previous example, we loaded a PDF, split it into chunks, created embeddings and stored them in a vector store DB. AWS Bedrock Knowledge Base can help automate all of above tasks. You just create a knowledge base on Bedrock, upload your PDFs etc. in S3 and provide S3 bucket as the source, and Knowledge Base will take care of creating a RAG store internally in AWS Opensearch Serverless. 

Other supported input mediums include Confluence (with auth credentials supplied via AWS secrets Manager), WebCrawler etc. Other supported RAG stores include Amazon Aurora, MongoDb Atlas, external Redis Enterprise Cloud etc.

Knowledge Base provides 2 sets of APIs to iteract with:
1. Retrieve API: Fetch RAG context from Knowledge Base, and then present it along with original question to FM.
2. Retrieve and Generate API: Single api that fetches context from RAG and then also invokes FM to return final response.

## About this POC
In this POC, we create a S3 bucket containing PDFs that we want to index into RAG. We then build a Knowledge base on top of this S3 bucket.
The given code is that of a lambda function which invokes Retrieve and Generate API on Knowldge base along with the FM ARN. The function is then able to answer queries based on knowledge from the PDFs.

Please note that AWS knowledge Base is billed on per hour basis, hence ensure that you delete the knowledge base at end of the POC.

As with previous examples, ensure Lambda as right IAM access, and timeout set to 1+ min.

Test Lambda with test prompt:
```
{
    "prompt" : "What is the deadline for submitting reimbursement form for FTT Fintech Festival?"
}
```