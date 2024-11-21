# Bedrock

## Bedrock Architectue

As shown in attached screenshot, Bedrock only creates an inference endpoint in AWS account. Clients can invoke it via Bedrock api. The base foundation model, or the fine tuned FMs are kept internally in an AWS owned Escrow account, and can't be accessed directly. any training data for fine tuning and creation of customer models should be placed in customer's AWS account.

If you are creating custom fine tuned model, then you can't keep using pay as you go model as with jsut using provided FMs. You will need to buy provisioned throughput with some time commitment.

Bedrock supports 2 modes of tuning base models:
1. Fine Tuning: With labelled data. For increasing the accuracy for specified tasks
2. Continued Pre-training: With unlablled data. To teach model a new domain of knowledge.

## Foundation model selection criterias
1. Type of modal. ie. Modality - text, image, video. Within text - if its summarisation type or chatbot type etc.
2. FM transparency index published by Stanford Institute.
3. Size, i.e. no. of params. Usually >50B is considered good enough to cover most of exhaustive use cases.
4. Inference Speed: Bigger the model, slower it can be. In the context of foundation models, parameters refer to the weights and biases adjusted during training.
   More parameters mean the model can capture more complex patterns and relationships in the data, but it also requires more computational resources
5. Context Window: Size of prompt you can feed to model at one point of time.

Roughly 75 words = 100 tokens. So if a model says that max tokens allowed is 4000, 
4000 X .75 = 3000 input words allowed at one point of time. 

6. Pricing. Eg. Claude is most expensive and almost 10 times more expensive than least expensive Titan model.
7. Training Data Sets: Choose FM based on what type of data they have been trained on.
   ie One or all of: Internet, Code, Human feedback etc.
8. Propriety vs Open source (preferred)
9. If model allows fine tuning or not. Not all of them allows it. 
10. Additional features like Multi-Lingual support.
11. Quality of response: Explained below.

## Quality of response
 FMs are evaluated based on following 3 factors:
 1. **Accuracy**: Measured using metrics like precision, recall, F1 score.
 2. **Toxicity**: Models tendency to generate inappropriate/harmful content.
 3. **Robustness**: A robust model is resilient to unexpected changes in input 
    data and can handle diverse and potentially noisy data. A measure to resist Adverserial attacks.

Bedrock provides 3 ways for Model Evaluation:
1. Automatic: Select the FM you want to evaluate, 
choose the metrics to evaluate on,
choose public data set provided for testing, 
or provide your own reference dataset along with responses.
Also give destination S3 bucket where evauation results would be stored.
2. Human - bring your own team
3. Human - AWS managed team
