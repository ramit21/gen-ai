# Chatbot with RAG

Enrich chatbot with PDF as external data source. Read the PDF, chunk it into segments, 
create embeddings (using Amazon Title FM) and store them in FAISS vector store.

Enrich user's prompt with knowledge store in FAISS, and then feed it to LLM model (Llama3) using LangChain, and return the response to Streamlit based UI.

## Installations
In addition to setups done in lab 3, install below as well:

```
 pip install flask-sqlalchemy
 pip install pypdf
 pip install faiss-cpu
 pip install -U langchain-community #for imports from langchain.embeddings

``` 
 
## Setup
Backend python file has all langchain chaining code that connects to Bedrock FM using a memory.

Streamlit history object is created in ui code and passed on as a param to the backend code creating the chain.

Run frontend to launch the UI application:
```
streamlit run .\chatbot_frontend.py
```

You may run >python chatbot_backend.py in isolation to test backend code with a standalone call to chain method.

## Info
Streamlit is Python based library for spinning up a quick UI, which will server as frontend for chatbot.

LangChain is a framework designed to help developers build applications powered by LLMs. Langchain provides many models, eg. **ConversationBufferMemory** to maintain chat history, and also provides **ConversationChain** to connect all these models.  

Notice how frontend code imports and invokes methods on backend to initialise memory, and then to pass it on calls to chain invoke method along with prompt.
