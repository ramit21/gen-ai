# Bedrock

## Bedrock Architectue

As shown in attached screenshot, Bedrock only creates an inference endpoint in AWS account. Clients can invoke it via Bedrock api. The base foundation model, or the fine tuned FMs are kept internally in an AWS owned Escrow account, and can't be accessed directly. any training data for fine tuning and creation of customer models should be placed in customer's AWS account.

If you are creating cstom fine tuned model, then you can't keep using pay as you go model as with jsut using provided FMs. You will need to buy provisioned throughput with some time commitment.

Bedrock supports 2 modes of tuning base models:
1. Fine Tuning: With labelled data. For increasing the accuracy for specified tasks
2. Continued Pre-training: With unlablled data. To teach model a new domain of knowledge.

