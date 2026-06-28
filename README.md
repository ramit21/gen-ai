# gen-ai
Generative AI concepts

## Deterministic vs non-deterministic AI models

Gen AI is a non-deterministic AI model, as it generates input based on randomness and probabilities. 

Traditional AI models can be deterministic or non-deterministic depending on their implementation. Here's a quick rundown:

Regression: Typically deterministic. Given the same input data, a regression model will produce the same output, such as predicting house prices or stock trends.

Clustering: Can be both. Methods like K-means can be non-deterministic due to random initialization, leading to different cluster assignments on different runs.

Reinforcement Learning: Often non-deterministic. The same action can lead to different outcomes due to the environment's dynamics and exploration strategies.

Classification: Usually deterministic. Algorithms like decision trees and logistic regression produce consistent results. However, models like neural networks can exhibit non-determinism due to random weight initialization.

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
 

**Pros that Gen AI will bring to society**
1. Increase productivity and efficiency.
2. Help with personalization.
3. Accessibility: Help people with disabilities. eg. provide real time translations, alternative formats etc.

**Risks and challenges of using Gen AI**:
1. Legal issues: 

1.1. Privacy: current models don't have a 'forgetting' feature for personal use; models are used on large amounts of data that may include someone's personal data.

1.2. Security. Traditional security measures do not suffice for GenAI, as it is undeterministic, works with natural langage, and uses unstrcutured data. Refer OWASP section below.

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

**MOE vs MOE models**

Mixture-of-Experts (MoE) models offer high-efficiency, fast-inference performance by activating only a subset of parameters per token, whereas dense models activate all parameters for every input. Eg of MOE: Gemma4, eg. of dense: Qwen3.5 models.

**VRAM vs RAM**

VRAM (Video RAM): This is the high-speed memory physically soldered onto your GPU. It is extremely fast but very limited in size (e.g., 8GB, 12GB, or 24GB on a high-end card).

When you run an LLM, the entire "brain" (the model weights) must be loaded into memory. The AI loader (like Ollama, LM Studio, or llama.cpp) checks the file size of the model:
 - If it fits: The model is placed entirely in VRAM. This is the "Gold Standard."
 - If it's too big: The loader has to make a choice. It can either offload some layers to the GPU and keep the rest in RAM, or run the whole thing in RAM.

The speed of an LLM is almost entirely determined by Memory Bandwidth—how fast the weights can be fed to the processor. VRAM feeds data to CPU very fast, and hence if model is mostly loaded into VRAM, it will perfrom fast. If most parts end up in RAM, the data flows very slowly to CPU. So even if you have a powerful CPU, the model will perform very slowly.

Thats why qunatization is used - to fit large models fit into small VRAM memory.

## OWASP LLM top 10

OWASP has come up with top 10 vunerabilities for LLMs just like they have a list for web security. Some of the top featured issues are:
1. Prompt injection
2. Sensitive info leakage
3. Supply chain vulnerabilities: Third-party models, datasets, or plugins - each one is a potential attack vector. Read about LightLLM attack.
4. System Prompt Leakage: By using role play; uses authoritative language to convince the model that they have the right to see the background code; asking model to give intermediate system instructions in a bse64 encoded output.
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

**Agents**: Langchain can integrate with various agents that generate some python code and run at the backend , eg QR code generator, CSV file processor etc. But since these Agents run code at backend based on user prompts, these come with their own set of risks. A promp injection attack can make a malicious code to run on server and have some ill effects like data leakage etc. Hence the input text must be properly sanitised before invoking agents. 
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

OR you can use Checkpoints, that stores the state of the chain in external DB, like Dynamodb.

https://python.langchain.com/v0.1/docs/modules/memory/types/buffer/.

**Langchain hub**: LangChain Hub is a platform where users can find and share commonly used prompts, chains, agents, 
and other components for building AI applications with LangChain. https://smith.langchain.com/hub

**LlamaIndex**: is an alternate framework to Langchain for developing LLM applications.
LangChain is more versatile and suitable for a wide range of NLP applications, while LlamaIndex excels in data indexing and retrieval tasks.

## LangGraph
LangGraph is a framework developed by LangChain for building stateful, multi-actor (incl human interaction), multi-agentinc applications. 
Think about different nodes in graph invoking different LLMs suited for that particular stage. Think about step functions with lambda as an analogy.

**LangGraph vs LangChain**: 

| LangChain | LangGraph | 
| -------- | -------- |
| Sequential chain - each step passes output to the next    | Graph based workflows -— nodes, edges, branching, loops, conditional routing    |
| Ephemeral state - state exists only during a single run; no built‑in persistence   | Persistent state — built‑in checkpointing, resumability, durable state across steps    |
| Simple chain— good for basic pipelines, RAG, prompt chains  | Agent‑style orchestration — supports multi‑step agents, tool use, retries, planning     |

**Observability** is even more important for multi-agent systems, not just for production reliability, but also because multi agent systems can quickly consume the allowed model tokens. Popular tools: Langfuse, Opik. For eg. when using Opik, the code looks like below, you put @track annotation to track a LLM node function.:
```
from opik import track

@track()
async def process_statement_workflow(file_path: str, user_id: str) -> OutputState:
```

**Memory types**:
1. Working Memory: short term, eg conversationBufferMemory. ie summary of conversation so far is fed back into LLM model calls, so that LLM can answer taking care of the ongoing conversation.
2. Episodic Memory: long term, vector similarity search, includes user interaction history.
3. Semantic Memory: long term, embeddings + metadata, includes user preference, domain knowledge, and other factual knowledge
4. Procedural Memory: long term, optimised prompts and workflow templates, key value based.

## Langraphs vs n8n

n8n is a low-code Workflow Automation tool. In 2026, n8n added a dedicated AI Agent Node. You drop an "AI Agent" node and select your Model (Claude/OpenAI). You can drag drop and create agents with memory, tool integrations or agent calling other agents (eg. delegating research work to an agent with lower cost LLM model). It integrates with external tools like Slack to send notifications, or buttons for human in the loop actions.

Use n8n when you main challenge is integrations and connectivities than LLM reasoning. 

LangGraph on the other half is a code-first framework (built on top of LangChain). Its primary job is to manage complex reasoning loops.

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
## EDD - Evaluation driven development
Most Gen AI POCs do not reach production, as gen ai is undermenisitc, and works on unstructured data. Hence POCs might start failing in prod with issues like hallucination, latency etc. Solution is EDD - where monitoring becomes part of your development from day 1. 

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

## AI Agents vs Agentic AI
An AI Agent is a specific software that invokes an LLM, along with external tools/API/databases to achieve a particular task. eg. Roo code (open source version of Cline). 
An AI agent can be zero-shot, few-shot (when the agent asks questions to gather more info before performing a task), or React docstore agent (uses a knowledge base to fetch specific information).

Agentic AI refers to an architectural framework or a system that exhibits high-level "agency." It coordinates multiple agents and tools to achieve a broad, complex goal. It is proactive. eg. Agentic AI.

In simple words, Agent = LLM + Harness, where LLM is the brain, HArness is the doer. A harness provides:

1. **Planning**: The ability to break down large tasks into smaller, manageable sub-goals (e.g., Reflection, Chain-of-Thought, or Tree-of-Thoughts). 
**ReAct** (Reasoning + Acting) paradigm is used to drive **"Agentic loops"**: Reason -> Select -> Execute -> Repeat

Breaking Down the Loop in the Harness:

Reason (Planning/Thinking): The harness prompts the LLM to analyze the current state and the user's ultimate goal. The LLM "thinks" about what it needs to do next (e.g., "I need to find the population of Paris in 2026. I should use a search tool.").

Select (Action Selection): Based on its reasoning, the LLM selects a specific tool from the toolkit provided by the harness, along with the arguments needed to run it (e.g., web_search(query="Paris population 2026")).

Execute (Action Execution): The harness takes over. The LLM cannot actually run code or browse the internet itself; the harness executes the selected tool, grabs the real-world result, and feeds that data back into the LLM's context window.

Repeat (Evaluation & Next Step): The harness asks the LLM to look at the new data, judge if the goal is met, and decide whether to loop again or present the final answer.

2. **Memory**: The capacity to store and recall information. This includes short-term memory (in-context learning and chat history) and long-term memory (external vector databases for retrieving information over time).
3. **Tools**: External capabilities the LLM can call upon to execute actions, such as APIs, web search engines, code execution environments, or databases.

**Guide and Sensors**:

These are used to assist in REACT loop. Guide are the contraints for the LLM Agent. Eg. of Guide: Steering file for the coding agent.

Sensors are the eyes and ears of LLM Agent, that provide feedback and help agent improve its output. Eg. Code reviewer/Linter.

How Sensors work: 
The agent executes an Output (Action).
This action changes the Environment (e.g., updates a database, runs a script, or searches the web).
The Sensors detect that change in the environment and pull in the new data (Observation).

This feedback drives the agent to adjust its next thought and move closer to the correct response.

### Sub Agents vs Agent teams
An agent can spin up multiple sub-agents for parallel processing, and block till all sub agents complete their processing. Each agent/subagent get their own context, tools, memory, and instructions to perfrom a job.

With agent teams, all the sub agents share a task list, and also communicate with each other, using **Medallion architecture** for sharing data.

----------------------------
## Deep Agents

Simple agents take a prompt, call an LLM, optionally use a few tools, and return a response.

**Deep Agents**, like coding agents (e.g., Kiro‑style architectures), are more advanced.  
They rely on four core components:

1. **[Planning](ca://s?q=Explain_agent_planning)** — breaking a large task into structured steps.
2. **[Sub‑agents](ca://s?q=Explain_sub_agents)** — specialised agents for tasks like planning, architecture, coding, testing, etc.
3. **[Virtual Filesystems](ca://s?q=Explain_agent_virtual_filesystem)** — memory, skills, summaries, and file‑like objects that persist across steps.
4. **[System prompts](ca://s?q=Explain_system_prompts)** — stable instructions that define behaviour, constraints, and persona.

Deep agents behave more like **multi‑step autonomous workers** than single‑shot LLM calls.


### Virtual Filesystem & Backends

Deep agents often use a **virtual filesystem (VFS)**.  
This is how coding agents can *read, write, modify, and track files* during multi‑step workflows.

The **backend** determines *where* this file data actually lives:

1. **StateBackend** (default)
- Lives **in RAM**, tied to a **single thread**.
- Fastest, but **not persistent**.
- Good for short‑lived agents or single‑session tasks.

2. **FilesystemBackend**
- Files are stored on the **real local filesystem**.
- Persistent across runs.
- Useful for coding agents that must generate actual files on disk.

3. **StoreBackend**
- Files live in a **LangGraph Store**, scoped by a namespace.
- Multiple threads or agents can access the same files.
- Enables:
  - shared memory
  - collaborative agents
  - long‑running workflows
  - resumable tasks


### Why This Matters

- Deep agents are **multi‑step**, **stateful**, and **tool‑driven**, unlike simple prompt‑response agents.
- They use **planning + sub‑agents** to break down complex tasks (e.g., code generation pipelines).
- A **virtual filesystem** allows agents to treat memory and files as first‑class objects.
- **Backends** determine persistence, concurrency, and scalability.
- StoreBackend is key for **multi‑agent systems**, **parallel execution**, and **resumability**.
- This architecture is foundational for **autonomous coding agents**, **workflow engines**, and **agentic AI systems**.

--
## RAG

Retrieval-Augmented Generation (RAG) is an AI architecture that supercharges Large Language Model (LLM) responses by dynamically fetching relevant, up-to-date information from an external knowledge source at inference time.

**Vector store vs Knowledge Graphs**

Both RAGs and knowledge graphs help enrich the context before invoking LLMs. The best approach is to use both if required, aka 'GraphRAG'.
Vector Store is well-suited for storing large volumes of unstructured data as embeddings, while KGs, stored in Graph DBs like Neo4j/Amazon Neptune, help store real-world relationships.

Eg, A graph KG of a customer to its accounts to its transactions. The prompt asks why this customer was blocked. The KG retrieval helps with the context of suspicious transactions that a customer would have performed.

More details in next section:

### RAG Types: Vector and Vectorless**

1. Vector (Dense Semantic retrieval):

1.1. Basic (Vector) RAG: Naive RAG is the foundational and most widely deployed RAG pattern. Documents are chunked, embedded via a model
such as text-embedding-ada or sentence-transformers, and stored in a vector database (ChromaDB, FAISS, Pinecone). At
query time the question is embedded and top-K nearest chunks are retrieved by cosine similarity, then injected into the LLM
prompt. Best for general Q&A chatbots, document search, and rapid prototypes where lexical precision is not critical.

1.2. Hybrid (Vector + Keyword): 2 searches are perfromed on the data - one usual vector search, and another sparse keyword search (using TF-IDF or BM25), and then merging the results using Reciprocal Rank Fusion (RRF). This dual-retrieval approach captures both semantic meaning and exact keyword matches,
boosting recall on technical queries, product codes, or named entities that pure vector search misses. Eg. Aurora PostgreSQL with the pgvector extension, Elasticsearch, Weaviate, and Pinecone.

2. Vectorless (Sparse/structured retrieval)

2.1. Keyword (BM25/TF-IDF): BM25 or TF-IDF — without any neural embeddings. This makes it extremely
fast, zero compute cost at inference, and highly precise for exact-term matching. It excels in domains with unique identifiers
such as medical codes, legal citations, part numbers, or financial tickers where semantic similarity is less relevant. Common
tools are Elasticsearch and OpenSearch.

2.2. Graph RAG (KG Traversal): Graph RAG stores knowledge as a property graph (nodes = entities, edges = relationships) and retrieves information via
graph traversal rather than similarity search. ie Search is performed based on bath and not cosine similarity. Eg. Neo4j, GraphRag.

2.3. SQL RAG (Text to SQL): The LLM translates a natural-language question into SQL, executes it
against a relational database, and uses the result as context for its final answer.

2.4. Reasoning (PageIndex): Reasoning RAG eschews chunking altogether. Documents are indexed as hierarchical tree structures and the LLM
traverses the tree step-by-step to locate relevant pages, reasoning about which branches to explore. This approach handles
very long documents — contracts, annual reports, legal briefs — far better than chunk-based methods because it preserves
document structure and avoids context fragmentation. Pioneered by **VectifyAI's PageIndex**; high complexity but
state-of-the-art quality on long-form document tasks.
Document is broken into branches based on TOC (Table of content), If no TOC present, then LLM is used to understand the document and then chunk.

### RAG Questions

Q. What evaluation metrics are used to assess RAG system quality?

A. Key metrics include: Context Precision (are retrieved chunks relevant?), Context Recall (are all necessary facts
retrieved?), Faithfulness (does the answer only use retrieved context, no hallucination?), and Answer Relevance (does
the answer address the query?). Frameworks like **RAGAS** automate these using **LLM-as-judge** evaluation.
Retrieval-level metrics (MRR, NDCG, Hit@K) measure retriever quality independently of the generator.

Q. What is the role of re-ranking in RAG pipelines?

A. Initial retrieval returns top-K candidates quickly but imprecisely. A re-ranker (cross-encoder model or LLM-as-judge) then
re-scores each candidate against the query with deeper computation, promoting the most relevant chunks before
passing them to the LLM. Re-ranking dramatically improves faithfulness and reduces noise in the context window.
Popular re-rankers include Cohere Rerank, BGE-Reranker, and FlashRank.

Q.What is semantic chunking and how does it differ from fixed-size chunking?

A. Semantic chunking splits documents at natural semantic boundaries — where topic or meaning shifts — rather than at
fixed token counts. It uses embedding similarity between consecutive sentences to detect boundaries: if adjacent
sentences diverge significantly in embedding space, a chunk boundary is inserted. This produces coherent,
self-contained chunks that improve retrieval precision compared to fixed-size chunks that can split sentences or mix
unrelated topics.

Q. What are the main failure modes of RAG systems and how do you mitigate them?

A. Key failure modes: (1) Retrieval failure — wrong chunks retrieved; mitigate with Hybrid RAG + re-ranking + query
rewriting. (2) Context window overflow — too many chunks exceed LLM limits; mitigate with tighter top-K and re-ranking.
(3) Hallucination despite retrieval — LLM ignores context; mitigate with faithfulness-focused prompting and citation
checks. (4) Stale index — outdated documents; mitigate with incremental indexing pipelines. (5) Prompt injection via
retrieved content; mitigate with input sanitisation and guard.

Q. Faiss vs Chromadb vs Pinecone

A. Faiss/Chromadb is good for local development, data saved in files on disk. Good for POCs, but doesn't scale. Pinecone is SAAS offering.

Faiss is good for fast retrieval speed, Chromadb is a more complete db with more features, eg. metadata based queries: "find similar documents, but only from PDF files uploaded in May," Chroma does this natively. 

### RAG techniques

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
7. **Cost reduction**: Regularly delete stale data to save on retieval costs. Cache frequent queries and RAG responses in Redis.

### ReBAC - Relationship based access control

RAG systems retrieve documents based on similarity, not permission. This creates a risk that data of one customer may become visible to the other. 
Traditional RBAC also can't be used here as it is not granular enough at document level.

Solution: use ReBAC.

To implement ReBAC, use Auth0 FGA. Here you define users, groups, and resources (PDF files being put into RAG), and relations on who can access what. Later when RAG store is queried, Auth0 FGA intercepts the request and forces RAG to be searched only for documents the user is allowed to access.

## Cost Optimisation with GenAI

1. **Right‑size models** — Use cheaper/smaller models for simple tasks; reserve expensive models for reasoning‑heavy steps.

2. **Control context growth** — Long conversations increase token cost. Periodically summarise and trim history.

3. **MCP server pruning** — Disable MCP servers you don’t need. Loading tool definitions consumes tokens at session start.

4. **Rule file optimisation** — Keep rule files short. Store pointers/links to long docs instead of embedding full content. Name + description act as metadata.

5. **Track usage** — Monitor context length (`/context`), token usage, and spend (`/cost`) to avoid silent cost creep.

6. **Use Memory for state** — Persist long‑term preferences or facts in Memory instead of re‑sending them every session.

7. **Vector DB cost control**  
   - Aurora PGVector = balanced cost/performance  
   - S3‑based vector stores = cheapest but higher latency

8. **RAG storage hygiene** — Remove outdated or unused documents to reduce storage and embedding costs.

9. **Semantic caching** — Add a semantic cache (e.g., Redis + embedding similarity). It checks *intent*, not exact text, before hitting the model.

10. **Model distillation** — Train a smaller model to mimic a larger one for your specific tasks. Cheaper + faster. Supported on Bedrock.

11. **Cloud optimisation** — Use reserved/spot instances and autoscaling inference endpoints.


## LLM Gateway
An LLM gateway is a middleware layer that sits between your application and multiple LLM providers.

**Core Features of LLM Gateways**:
1. Unified API — Call any model (OpenAI, Groq, Anthropic, HF) using the same request format and methods.
2. Model routing — Automatically choose the best model based on cost, latency, or quality.
3. Fallback handling — If one provider fails, the gateway retries with another.
4. Rate‑limit smoothing — Queue or distribute requests to avoid hitting provider limits.
5. Centralised logging — One place to view all prompts, responses, and latency metrics.
6. Cost tracking — Track spend per model, per user, per endpoint.
7. Key management — Store API keys in one secure place instead of scattering them across services.
8. Caching — Cache identical prompts to reduce cost and latency.
9. Fine‑grained access control — Control which teams or services can use which models.

**LiteLLM** is a lightweight gateway that exposes a single OpenAI‑compatible API but routes to any backend model (Groq, Anthropic, Gemini, Llama, etc.).

Sample code that shows how LiteLLM routes request to another model should primary fail:
```
import litellm
from litellm import Router
from langchain_openai import ChatOpenAI
import threading

# -----------------------------
# 1. Configure LiteLLM Router in code
# -----------------------------
router = Router(
    model_list=[
        {
            "model_name": "smart-llm",
            "litellm_params": {
                "model": "groq/mixtral-8x7b",
                "api_key": "GROQ_KEY"
            },
            "fallback_models": [
                "openai/gpt-4o",
                "anthropic/claude-3-haiku"
            ]
        },
        {
            "model_name": "openai/gpt-4o",
            "litellm_params": {
                "model": "openai/gpt-4o",
                "api_key": "OPENAI_KEY"
            }
        },
        {
            "model_name": "anthropic/claude-3-haiku",
            "litellm_params": {
                "model": "anthropic/claude-3-haiku",
                "api_key": "ANTHROPIC_KEY"
            }
        }
    ]
)

# -----------------------------
# 2. Start LiteLLM server in background thread
# -----------------------------
def start_server():
    litellm.run(port=4000, router=router)

thread = threading.Thread(target=start_server, daemon=True)
thread.start()

# -----------------------------
# 3. LangChain client pointing to LiteLLM
# -----------------------------
llm = ChatOpenAI(
    model="smart-llm",                 # triggers fallback chain
    openai_api_key="dummy",            # ignored by LiteLLM
    openai_api_base="http://localhost:4000"
)

# -----------------------------
# 4. Make a request
# -----------------------------
response = llm.invoke("Explain how LLM fallback works in one paragraph.")
print(response)

```
A good youtube video by Krish Naik: https://www.youtube.com/watch?v=RN3baOpNA6w
----------------------------
## LLMOps
[📘 LLM OPS](./llmOps.md)
----------------------------
## Ollama
[📘 View the full Ollama Course](./ollama.md)
----------------------------
## GenAI for Coding
[📘 Use of GenAI for coding Course](./GenAI_for_Coding_Course.md)
----------------------------
## Langraph POC
https://github.com/ramit21/langraph-coder-buddy

Youtube video: https://www.youtube.com/watch?v=SP-b_G74Nuk


