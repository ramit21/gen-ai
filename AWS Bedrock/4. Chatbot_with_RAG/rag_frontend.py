import streamlit as st
import rag_backend as demo # import backend file

st.title("RAG demo")

new_title='<p style="font-family:sans-serif; color:Green; font-size:42px;">HR Q&A with RAG'
st.markdown(new_title, unsafe_allow_html=True)

# load index first time
if 'vector_index' not in st.session_state:
    with st.spinner("Indexing data into vector store ..."):
        st.session_state.vector_index = demo.hr_index()

input_text = st.text_area("Input Text", label_visibility="collapsed")
send_button = st.button("Send", type="primary")

#On submit of question, invoke the LLM chain, that leverages the indexed RAG and returns with relevant answer
if send_button:
    with st.spinner("Loading response ..."):
        response_content = demo.hr_rag_response(index=st.session_state.vector_index, question=input_text)
        st.write(response_content)
