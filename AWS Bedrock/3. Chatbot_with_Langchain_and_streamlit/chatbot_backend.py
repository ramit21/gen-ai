from langchain.chains import ConversationChain
from langchain.memory import ConversationSummaryBufferMemory
from langchain_aws import ChatBedrock

#Funtion for invoking the model
def demo_chatbot():
    # google 'amazon bedrock inference parameters' to get below parameters for Anthropic Claude
    llm = ChatBedrock(
        credentials_profile_name='default', # The AWS profile configured on your system
        model_id='us.meta.llama3-2-1b-instruct-v1:0',
        model_kwargs = {
            "temperature": 0.1,
            "top_p": 0.3
        }
    )
    return llm

#Function for memory creation
def demo_memory():
    llm = demo_chatbot()
    memory = ConversationSummaryBufferMemory(llm=llm, max_token_limit=300)
    return memory

#Function for creating chain = Input text + memory
def demo_conversation(input_text, memory):
    llm = demo_chatbot()
    llm_conversation = ConversationChain(llm=llm, memory=memory, verbose=True)
    chat_reply = llm_conversation.invoke(input_text)
    return chat_reply['response']

print(demo_conversation('Hi', demo_memory())) #to test backend code with >python chatbot_backend.py

