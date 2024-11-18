# Langchain and Streamlit based chatbot

Chat solutions need to have memory as FMs are stateless. This is needed to support chat flow, eg user prompts 'give me top 3 things to do in Paris', and then user asks 'give me next 3'. Chat solution can answer second question correctly only if it has some form of memory of what it has already answered.

The prompt input is augmented with chat history and fed to the model, and on response from model, the history is updated. Langchain can take care of these interactions with the memory for us.

## Installations
Install AWS CLI, Python, Langchain and Steamlit on your system.

Configure AWS profile on your system that has access to the Bedrock FM.

Open Anaconda, and (must) launch visual studio from there, then go to terminal and start with the installations.

```
 python -m ensurepip --upgrade  #install pip
 pip install boto3
 pip show boto3 # check installation and the version installed
 pip install langchain
 pip install streamlit
 streamlit hello # starts streamlit server on Python
 pip install -U langchain-aws
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
