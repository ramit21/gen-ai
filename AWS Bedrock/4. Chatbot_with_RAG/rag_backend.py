from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_aws import BedrockEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.indexes import VectorstoreIndexCreator

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
