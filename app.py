import streamlit as st
import os
from groq import Groq
import random
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os 

load_dotenv()

groq_api_key = os.environ['GROQ_API_KEY']

def main():
    # Customizing UI with background, emojis, and colors #f0f0f0
    st.markdown(
        """
        <style>
        .reportview-container {
            background-image: url('https://link_to_your_image.jpg');
            background-size: cover;
        }
        h1 {
            color: #4284f5;
            font-size: 40px;
            font-weight: bold;
        }
        .sidebar .sidebar-content {
            background-color: #a9e670; 
        }
        </style>
        """, unsafe_allow_html=True
    )
    
    st.title("Groq Chat App 🤖💬")

    # Sidebar
    st.sidebar.title('Select an LLM 🔍')
    model = st.sidebar.selectbox(
        'Choose a model 🤖',
        ['mixtral-8x7b-32768', 'llama2-70b-4096'],
        format_func=lambda x: f"{x} 🧠"
    )
    conversational_memory_length = st.sidebar.slider('Conversational memory length:', 1, 10, value = 5)

    memory = ConversationBufferWindowMemory(k=conversational_memory_length)

    user_question = st.text_area("Ask a question 🧐:")

    # session state variable
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history=[]
    else:
        for message in st.session_state.chat_history:
            memory.save_context({'input': message['human']}, {'output': message['AI']})

    # Initialize Groq Langchain chat object and conversation
    groq_chat = ChatGroq(
        groq_api_key=groq_api_key, 
        model_name=model
    )

    conversation = ConversationChain(
        llm=groq_chat,
        memory=memory
    )

    submit_button = st.button(label='Ask Question ❓')

    if submit_button and user_question:
        with st.spinner('Thinking... 🤔'):
            response = conversation(user_question)
            message = {'human': user_question, 'AI': response['response']}
            st.session_state.chat_history.append(message)
            st.write("Chatbot 🤖:", response['response'])

if __name__ == "__main__":
    main()
