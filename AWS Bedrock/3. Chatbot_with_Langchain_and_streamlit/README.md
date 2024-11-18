# Langchain and Streamlit based chatbot

Chat solutions need to have memory as FMsare stateless. This is needed to support chat flow, eg user prompts 'give me top 3 Cricket players', and then user asks 'give me next 3'. Chat solution can answer it correctly only if it has some form of memory.

## Installations
Install AWS CLI, Python, Langchain and Steamlit on your system.

Open Anaconda, and (must) launch visual studio from there, then go to terminal and start with the installations.

```
 python -m ensurepip --upgrade  #install pip
 pip install boto3
 pip show boto3 # check installation and the version installed
 pip install langchain
 pip install streamlit
 streamlit hello # starts streamlit server on Python
 pip install -U langchain-aws
 pip install anthropic
``` 
 
## Setup

```
python chatbot_backend.py
python chatbot_frontend.py
```

Streamlit is Python based library for spinning up a quick UI, which will server as frontend for chatbot.

LangChain is a framework designed to help developers build applications powered by LLMs. Langchain provides many models, eg. **ConversationBufferMemory** to maintain chat history, and also provides **ConversationChain** to connect all these models.  

