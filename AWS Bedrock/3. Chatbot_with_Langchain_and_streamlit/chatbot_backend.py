from langchain.chains import ConversationChain
from langchain.memory import ConversationSummaryBufferMemory
from langchain_aws import ChatBedrock

def demo_chatbot(input_text):
    # google 'amazon bedrock inference parameters' to get below parameters for Anthropic Claude
    llm = ChatBedrock(
        credentials_profile_name='default',
        model_id='us.anthropic.claude-3-5-haiku-20241022-v1:0',
        model_kwargs = {
            "temperature": 0.1,
            "top_p": 0.9,
            "max_tokens": 300,
            "stop_sequences": ["\n\nHuman:"]
        }
    )
    return llm.invoke(input_text)

response = demo_chatbot(input_text="Hi, what is your name?")
print(response)

