# Bedrock

## Bedrock Architectue

As shown in attached screenshot, Bedrock only creates an inference endpoint in AWS account. Clients can invoke it via Bedrock api. The base foundation model, or the fine tuned FMs are kept internally in an AWS owned Escrow account, and can't be accessed directly. any training data for fine tuning and creation of customer models should be placed in customer's AWS account.

