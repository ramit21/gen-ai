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
1. MLOps focuses on training a model from scratch, LLMOps more on fine tuning an existing model.
2. MLOps evluates well defined metrics like F1 Score, recall, wheras LLMOps relies on more complex metrics like Bleu score, human feedback etc.
3. MLOps tracks model drift and performance, LLMops tracks prompts and completion pairs (ouput token length, latency etc)

Popular LLMOps tools: Google cloud vertex AI, Databricks, Valohi, Ollama, BentoML, Kubeflow etc.
 

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
 
**LangGraph**: LangGraph is a framework developed by LangChain for building stateful, multi-actor (incl human interaction), multi-agentinc applications. 
Think about different nodes in graph invoking different LLMs suited for that particular stage. Think about step functions with lambda as an analogy.

**LangGraph vs LangChain**: 

| LangChain | LangGraph | 
| -------- | -------- |
| Sequential chain    | Graph based workflows     |
| Limited state management   | Advanced persistent state     |
| Simple chain  | Advanced persistent state     |

Observability is even more important for multi-agent systems, not just for production reliability, but also because multi agent systems can quickly consume the allowed model tokens. Popular tools: Langfuse, Opik.

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
----------------------------
## Ollama
[📘 View the full Ollama Course](./ollama.md)
----------------------------
## GenAI for Coding
[📘 Use of GenAI for coding Course](./GenAI_for_Coding_Course.md)
----------------------------
## OpenAI

OpenAI provides APIs for chat completion, text generation, moderation, and several specialised model families. For text‑based tasks, it offers models like 'GPT‑4' and 'GPT‑3.5'. For audio, OpenAI provides 'Whisper' for speech‑to‑text transcription. For image generation, it offers 'DALL·E', and for video generation, newer models ('Sora') extend that capability further. Each API endpoint is designed for a specific modality, making it easy to integrate natural language, audio, and visual intelligence into applications.

'CLIP (Contrastive Language–Image Pre‑training)' is an OpenAI model that learns the relationship between images and text. It uses separate image and text encoders to map both into a shared vector space, allowing it to match pictures with their correct descriptions. CLIP enables zero‑shot image classification, improves prompt understanding, and acts as the vision‑language backbone for many generative models like DALL·E and Stable Diffusion. e.g., use case for the CLIP model: flag  inappropriate images uploaded by end users.

Useful code demos:
- https://www.youtube.com/watch?v=y8-En6J9o-Y
- https://www.youtube.com/watch?v=HbY51mVKrcE
- https://www.youtube.com/watch?v=XMrtHz4IoT0
- https://www.youtube.com/watch?v=b7qhSmUQ9oo
- https://www.youtube.com/watch?v=VVKcSf6r3CM
- https://www.youtube.com/watch?v=kj6Zb_KGz0g
- https://www.youtube.com/watch?v=MmtVJmcOYDg
----------------------------
## Fine-tuning and Preference Alignment
**Fine-tuning**: Train the model on new data, but change only a few parameters (weights and biases), considering the cost of a full training in mind. A full pre-training, for example, TinyLlama, a model with 1.1B parameters, requires 16 A100-40G GPUs to run for 90 days. Training data is usually provided as files, which is tokenised before being used for training. Don't confuse using RAG for training, as it is more for inference.

2 popular techniques:
1. LoRA (Low Rank Adoption): Update a small no of parameters
2. QLoRA (Quantised LoRA): Uses even less memory than LoRA as it works on quantised numbers. This type of fine tuning can even be done on regular computers.

**Preference Alignment**: Preference Alignment is a critical phase in AI training where a model is fine-tuned to ensure its outputs match human values, safety standards, and specific user expectations. Without alignment, an AI is just a mirror of the internet—it can be biased, toxic, or dangerous.

2 popular techniques:
1. **RLHF (Reinforcement Learning from Human Feedback)**: Eg. Model produces 2 outputs that the human then selects, and the model learns from the selection. This technique is also called **PPO (Proximal Policy Optimization)**.
2. **DPO (Direct Preference Optimization)**: Getting more popular. It looks at the "Better" and "Worse" pairs and directly adjusts the AI's internal math to increase the probability of the good answer while decreasing the bad one. 

## Evaluation
### Traditional metrics

1. Word Error Rate (WER):

Used primarily in speech recognition and machine translation. 

Measures the edit distance between a reference text and the system output

Calculated as: (Substitutions + Insertions + Deletions) / Number of Words in Reference

Lower WER indicates better performance

2. Exact Match (EM):

Used in question answering and other tasks requiring precise answers

Binary metric: 1 if the predicted answer exactly matches the reference, 0 otherwise

Simple but strict; doesn't account for partial correctness

3. BLEU (Bilingual Evaluation Understudy):

Primarily used in machine translation

Measures the overlap of n-grams between the reference and candidate translations

Scores range from 0 to 1, with 1 being a perfect match

Criticised for not always correlating well with human judgments

4. ROUGE (Recall-Oriented Understudy for Gisting Evaluation):

Used mainly in text summarisation

Measures the overlap between generated summaries and reference summaries

Various versions: ROUGE-N (n-gram overlap), ROUGE-L (longest common subsequence), etc.

Higher ROUGE scores indicate better performance

### Embedding Based Methods

These methods leverage the power of dense vector representations of words, sentences, or documents to assess similarity and quality in a more nuanced way than traditional lexical-matching metrics.

1. BERTScore: Uses contextual embeddings from models like BERT. Computes pairwise cosine similarities between tokens in candidate and reference texts. Claims to correlate better with human judgments than traditional metrics
2. MoverScore: Combines Word Mover's Distance with contextual embeddings. Balances semantic similarity with token importance.
3. BLEURT (Bilingual Evaluation Understudy with Representations from Transformers: Fine-tunes a pre-trained language model on human ratings. Produces a learned metric that correlates well with human judgments.

### Evaluation tools
OpenAI Evals, Ragas (for evaluating RAGs), LangSmith (monitor LLM application), Hugging Face Evaluate, EleutherAI LM Evaluation Harness
----------------------------
## Development using LLM

You can access LLM models either via the internet by paid subscriptions, or by deploying open-source models like lama3 locally. Web environments like Google Colab and Lightning Studio allow you to access GPUs with pay-as-you-go model. You can access open-source models via HuggingFace, Groq, or Ollama.
----------------------------
## RAG techniques

 RAG techniques that help improve the performance of LLM applications:

1. **Context Enrichment Window**: While chunking the data before uploading to RAG, maintain some overlap. This helps maintain some context between different chunks, and that helps the retrieval process.
2. **Fusion Retrieval**: This system integrates two powerful document retrieval techniques: vector-based similarity search and keyword-based BM25 retrieval. By leveraging the strengths of both approaches, the Fusion Retrieval system aims to enhance the quality and relevance of the retrieved documents. BM25 works similarly to TF-IDF in search engines; it looks at the frequency of the input query in the chunks and ranks the documents accordingly. The Vector search and BM25 search are performed in parallel, and the results are then fused and reranked using the 'Reciprocal rank fusion' algorithm, which finally returns the top k documents. Read more here - https://varunbhanot.substack.com/p/day-16-going-beyond-basic-rag-part
3. **Query Transformation**: The input prompt is rewritten to make it more impactful before fetching the RAG. 3 types:
   3.1. Query rewriting: Reformulates queries to be more specific and detailed, improving the likelihood of retrieving relevant information.
   3.2. Step-back Prompting: Generates a higher-level query for RAG retrieval. e.g., if the prompt is asking about 'machine learning', the step back would change it to 'artificial intelligence' to make it more generic.
   3.3. Sub-query Decomposition: breaks down complex queries into simpler sub-queries, enabling the retrieval of information covering different aspects of a complex query.
4. **Reranking**: After similarity search retrieval from RAG, use LLM or a Cross Encoder to re-rank the results.
5. **Feedback Loop**: User feedback is taken on the generated output. The vector store is frequently updated as per user feedback.
6. **Adaptive RAG system**: adapt the retrieval strategy based on the type of query. By leveraging Language Models (LLMs) at various stages, we can provide more accurate and relevant information to users. Apply different retreival based on prompt intention: factual, analytical, opinion, contextual (user input). 

----------------------------
## AI Agents vs Agentic AI
An AI Agent is a specific software that invokes an LLM, along with external tools/API/databases to achieve a particular task. eg. Roo code (open source version of Cline). 
An AI agent can be zero-shot, few-shot (when the agent asks questions to gather more info before performing a task), or React docstore agent (uses a knowledge base to fetch specific information).

Agentic AI refers to an architectural framework or a system that exhibits high-level "agency." It coordinates multiple agents and tools to achieve a broad, complex goal. It is proactive. eg. Agentic AI.

----------------------------
## RAG - Vector store vs Knowledge Graphs

Both RAGs and knowledge graphs help enrich the context before invoking LLMs. The best approach is to use both if required, aka 'GraphRAG'.
Vector Store is well-suited for storing large volumes of unstructured data as embeddings, while KGs, stored in Graph DBs like Neo4j/Amazon Neptune, help store real-world relationships.
Eg, A graph KG of a customer to its accounts to its transactions. The prompt asks why this customer was blocked. The KG retrieval helps with the context of suspicious transactions that a customer would have performed.



