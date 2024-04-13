# gen-ai
Generative AI concepts

## AI fundamentals

**LLM flavours**:
1. Open source models: eg. Data bricks dolly, Meta Llama, mosaic mpt, Hugging face, Stable Diffusion etc. More control on tuning the model to your use case, eg. tuning the model on sample data that is more specific to your use insead of a large data corpus. Cons: requires in house expertise, needs time to evaluate and tune the model.
2. Proprietary models: LLM-as-a-service. eg ChatGPT. Quick to get started. Cons: Pay per token sent/received, vendor lockin, data/privacy issues - you may not know how your data is used.

**Chaining of LLM models**: You might need to run a workflow of multiple tasks. eg if you pass in a large corpus of documents for sentiment analysis, the inference point may get overwhelmed. Instead, if you first summarise the documents, and then do sentment anaylsis, it gives better results. Tools like Langchain, Haystack, txtai help in chaining of models like this.

**Lakehouse AI**: A Datafabric offering for Data + LLM AI. A data centric AI platform. Collect data (and store in say vector DB), use existing or custom build models, serve the models and monitor.

**Strategic roadmap for AI adoption**: 
1. Define GenAI strategy: define success criteria, engage busiess units, setup legal policies.
2. Identify business use case.
3. Design and architecture: choose the right AI model architecture.
4. Operation and Monitoring.
5. People and adoption: Train people, and refine roles.

**Q. How is LLMOps different to MLOps:**
1. Internal/external model hub: designed for managing LLMs specifically designed for fine tuning.
2. Fine tuning the model
3. Vector Database
4. Model Serving - specialised real time APIs for deployed LLM models
5. Human feedback in monitoring and evaluation.

**Pros that Gen AI will bring to soceity**
1. Increase productivity and efficiency.
2. Help with personalization.
3. Accessibility: Help people with disabilities. eg. provide real time translations, alternative formats etc.

**Risks and challenges of using Gen AI**:
1. Legal issues: 

1.1. Privacy: current models don't have a 'forgetting' feature for personal use; models are used on large amounts of data that may include someone's personal data

1.2. Security of the model: eg. 'prompt injection' to generate for malicious code, or make the model reveal confidential/incorrect information.

1.3. Intellectual Property protection: models may come with legal terms and condition on how it should be used, and or if it can be used for commercial purpose etc. There are multiple region specific AI regulations also coming up quick and fast that one needs to adhere to.

2. Ethical issues: Bias (bias can get added to the model due to the sampled data for fine tuning or human feedback adds to bias), misinformation (hallucination) 
3. Social/Environmental issues: impact on workforce and environment.

**2 types of Hallucination**:
1. Intrinsic: Model produced wrong output than the data it is trained on. 
2. Extrinsic: Model produces an output which can neither be proven right nor wrong based on the data it is trained on.

**Mitigating above issues with LLM models**:
1. Data bias: Assess against multiple small data slices, and keep updaing the data used for fine tuning.
2. Toxic/confidential output: Apply Gaurdrails, assess data qulity using tools like SparkNLP etc.
3. Misinformation: Curate the outputs, and fine tune wherever required.
4. Malicious use: Regulation

**3 Layered approach for auditing Gen AI models:**:
1. Governance auditing: around the companies that provide the models.  
2. Model auditing: auditing the model before public release.
3. Application auditing: assess the risk based on user utilisation. 


