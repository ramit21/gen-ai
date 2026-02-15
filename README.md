# gen-ai
Generative AI concepts

## Gen AI fundamentals

**Language Modeling**: Given a sequence of words, predicting the next word with highest probability.

**LLM**: A language model with large no of parameters. These are trained on huge amount of data, which is used to calculate good probabilities of next word in the sequence.

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

1.1. Privacy: current models don't have a 'forgetting' feature for personal use; models are used on large amounts of data that may include someone's personal data.

1.2. Security of the model: eg. 'prompt injection' to generate for malicious code, or make the model reveal confidential/incorrect information.

1.3. Intellectual Property protection: models may come with legal terms and condition on how it should be used, and or if it can be used for commercial purpose etc. There are multiple region specific AI regulations also coming up quick and fast that one needs to adhere to.

2. Ethical issues: Bias (bias can get added to the model due to the sampled data for fine tuning or human feedback adds to bias), misinformation (hallucination) 
3. Social/Environmental issues: impact on workforce and environment.

**2 types of Hallucination**:
1. Intrinsic: Model produced wrong output than the data it is trained on. 
2. Extrinsic: Model produces an output which can neither be proven right nor wrong based on the data it is trained on.

**Mitigating above issues with LLM models**:
1. Data bias: Assess against multiple small data slices, and keep updaing the data used for regular fine tuning.
2. Toxic/confidential output: Apply Gaurdrails, assess data quality using tools like SparkNLP etc.
3. Misinformation: Curate the outputs, and fine tune wherever required.
4. Malicious use: Regulation.

**3 Layered approach for auditing Gen AI models:**
1. Governance auditing: around the companies that provide the models.  
2. Model auditing: auditing the model before public release.
3. Application auditing: assess the risk based on user utilisation. 

** Deterministic vs non-deterministic AI models:**

Gen AI is a non-deterministic AI model, as ite generates input based on randomness and probabilities. 

Traditional AI models  can be deterministic or non-deterministic depending on their implementation. Here's a quick rundown:

Regression: Typically deterministic. Given the same input data, a regression model will produce the same output, such as predicting house prices or stock trends.

Clustering: Can be both. Methods like K-means can be non-deterministic due to random initialization, leading to different cluster assignments on different runs.

Reinforcement Learning: Often non-deterministic. The same action can lead to different outcomes due to the environment's dynamics and exploration strategies.

Classification: Usually deterministic. Algorithms like decision trees and logistic regression produce consistent results. However, models like neural networks can exhibit non-determinism due to random weight initialization.

----------------------------

## Types of Gen AI models

https://www.forbes.com/sites/bernardmarr/2024/04/29/the-4-types-of-generative-ai-transforming-our-world/?sh=33c2c8a2eb3a

## LangChain

LangChain is a programming language platform that allows developers to create and connect models to access, transform, and share data. It's designed to help developers build applications that use LLMs, such as chatbots and virtual agent.

**LCEL**: LangChain Expression Language is a declarative way to compose chains of tasks in LangChain.

**React Agents**: The ReAct (Reason+Act) means think about the problem, break it into smaller tasks and interact with external environments to perform a complex task. 
React Agents are designed to enable language models to interact with external tools and perform tasks that require both reasoning and action.
An **agent executor** is used to manage the interactions between the language model and the tools.

**Callback handlers**: LangChain provides a callback system that allows you to hook into various stages of your LLM application. Several callback event are supported like - LLM/Chain/Tool - start/end/errors etc.

**RAG data indexing parameters**: When indexing data (from text files, pdf, scraped websites etc) for storing in RAG, 2 important parameters:
1. **Chunk size**: No. of tokens in the chunk size. Choose it wisely as per the tokens allowed in the eventual LLM used. 
To understand this, let's say we fetch top 5 contexts from RAG and provide it to the LLM model, and each chunk size is say 200 tokens, then we have already
added 5X200=1000 tokens as RAG context to the input prompt tokens, leaving little room for output token count.   
2. **Overlap**: How many tokens overlap between different chunks. This decides contextual continiuity between different chunks.
An overlap of 0 means all chunks are treated separately. And, too much overlap can lead to redundancy and inefficiency.

You can use Langchain text split playground to play with your data and arrive at optimal chunk size and overlap values - https://langchain-text-splitter.streamlit.app/.

**Firecrawl**: It is a SAAS tool that is used to scrape website urls, and create RAG vector strore embeddings. It integrates very easily with Langchain. 

**Agents**: Langchain can intgrate with various agents that generate some python code and run at the backend , eg QR code generator, CSV file processor etc. But since these Agents run code at backend based on user prompts, these come with their own set of risks. A promp injection attack can make a malicious code to run on server and have some ill effects like data leakage etc. Hence the input text must be properly sanitised before invoking agents. 
Also, the use of Agents can be flaky - different answers to same query.

Agent router is used to send different user inputs to different agents based on description fields..

**Langchain Tools**: These expoe common functions which are supported by most LLM models. 
Before Langchain tools, one had to call LLM vendor specific functions.
Lanchain tools help abstract it, and calls the underlying model's API as per the implementation. Helps save lot of code with Langchain.

**Tavily**: Tavily is primarily designed as a search engine for Large Language Models (LLMs) and AI agents, providing real-time, accurate search results and information retrieval. Tavily is optimised for RAGs and integrates very well with LangChain.

**Memory**: Langchain supports different type of memories, for example:
1. ConversationSummary: updates the summary on every user interation,
2. ConversationBuffer: keeps track of all interactions, can end up consuming lot of memory if conversation size grows.
3. ConversationWindowBuffer: keeps track of last k (window size) interactions.
4. ConversationTokenBuffer: keeps conversations upto specified token count.
5. Backed by vector store: save user interactions as embeddings in the vector store. This adds to latency and cost.

https://python.langchain.com/v0.1/docs/modules/memory/types/buffer/.
 
**LangGraph**: LangGraph is a framework developed by LangChain for building and scaling agentic applications. 
It allows developers to create stateful, multi-actor (incl human interaction) applications using LLMs.
Think about step functions with lambda as an analogy.

**Langchain hub**: LangChain Hub is a platform where users can find and share commonly used prompts, chains, agents, 
and other components for building AI applications with LangChain. https://smith.langchain.com/hub

**LlamaIndex**: is an alternate framework to Langchain for developing LLM applications.
LangChain is more versatile and suitable for a wide range of NLP applications, while LlamaIndex excels in data indexing and retrieval tasks.

## Token limitation

If input and output combined token counts exceeds token limit then LLM errors out. 
Techniques are available to manage LM token limit issue:

For eg., let's say we have to process 10 documents, and produce a summary output using LLM.

1. **Stuff**: all the documents together and then feed to LLM.
```
from langchain.chains.summarize import load_summarize_chain

chain = load_summarize_chain(llm, chain_type="stuff")

```

2. **Map Reduce**: Summarize all documents through LLM in parallel, and then combine and summarise from all the summaries generated.
```
chain = load_summarize_chain(llm, chain_type="map_reduce")
```
Because of parralelism, it is faster, but con is that multiple api calls can increase the cost, and there can be loss of information as we generate final summay from ther summaries. 

3. **Refine**: Multiple iterations of summarising documents, till a good level of details is preserved.
```
chain = load_summarize_chain(llm, chain_type="refine")
```

## Ollama
[📘 View the full Ollama Course](./ollama.md)

## GenAI for Coding
[📘 Use of GenAI for coding Course](./GenAI_for_Coding_Course.md)

## OpenAI

OpenAI provides APIs for chat completion, text generation, moderation, and several specialised model families. For text‑based tasks, it offers models like 'GPT‑4' and 'GPT‑3.5'. For audio, OpenAI provides 'Whisper' for speech‑to‑text transcription. For image generation, it offers 'DALL·E', and for video generation, newer models ('Sora') extend that capability further. Each API endpoint is designed for a specific modality, making it easy to integrate natural language, audio, and visual intelligence into applications.

Useful code demos:
- https://www.youtube.com/watch?v=y8-En6J9o-Y
- https://www.youtube.com/watch?v=HbY51mVKrcE
- https://www.youtube.com/watch?v=XMrtHz4IoT0
- https://www.youtube.com/watch?v=b7qhSmUQ9oo
- https://www.youtube.com/watch?v=kj6Zb_KGz0g
- https://www.youtube.com/watch?v=MmtVJmcOYDg
