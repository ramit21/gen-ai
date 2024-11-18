from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_aws import BedrockEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.indexes import VectorstoreIndexCreator
from langchain_aws import ChatBedrock

# function to read and index external data
def hr_index():
    # Load data source PDF using PyPdfLoader
    data_load=PyPDFLoader('https://www.upl-ltd.com/images/people/downloads/Leave-Policy-India.pdf')
    # Split data based on character
    data_split=RecursiveCharacterTextSplitter(separators=["\n\n", "\n", " ", ""], chunk_size=100,chunk_overlap=10)
    #Create embeddings
    data_embeddings=BedrockEmbeddings(
        credentials_profile_name='default',
        model_id='amazon.titan-embed-text-v1'
    )
    data_index=VectorstoreIndexCreator(
        text_splitter=data_split,
        embedding=data_embeddings,
        vectorstore_cls=FAISS
    )
    db_index=data_index.from_loaders([data_load])
    return db_index

def hr_llm():
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

def hr_rag_response(index, question):
    rag_llm=hr_llm()
    hr_rag_query=index.query(question=question,llm=rag_llm)
    return hr_rag_query

# print(hr_rag_response(hr_index(), 'How many annual leaves allowed?')) #test with > python rag_backend.py
