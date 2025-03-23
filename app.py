import streamlit as st
import os
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load environment variables first
load_dotenv()

# Get API Key
groq_api_key = os.getenv("GROQ_API_KEY")  # ✅ Fix: Use os.getenv() to avoid errors

# Customizing UI
st.markdown(
    """
    <style>
    .reportview-container {
        background-image: url('https://images.wallpapersden.com/image/download/surreal-psychedelic-landscape-amazing-ai-art_bmdlam6UmZqaraWkpJRobWllrWdma2U.jpg');
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
    """,
    unsafe_allow_html=True
)

# Streamlit Title
st.title("Groq Chat App 🤖💬")

# Sidebar: Model Selection
st.sidebar.title('Select an LLM 🔍')
model = st.sidebar.selectbox(
    'Choose a model 🤖',
    ['llama-3.3-70b-versatile', 'mixtral-8x7b-32768', 'llama-3.1-8b-instant'],
    format_func=lambda x: f"{x} 🧠"
)

# Conversational Memory Length
conversational_memory_length = st.sidebar.slider('Conversational memory length:', 1, 50, value=10)

# Initialize Memory
memory = ConversationBufferWindowMemory(k=conversational_memory_length)

# User Input Box
user_question = st.text_area("Ask a question 🧐:")

# Initialize Chat History
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
else:
    for message in st.session_state.chat_history:
        memory.save_context({'input': message['human']}, {'output': message['AI']})

# Initialize ChatGroq Model
groq_chat = ChatGroq(
    groq_api_key=groq_api_key,  # ✅ Fix: Now the API key is properly loaded
    model_name=model
)

# Create Conversation Chain
conversation = ConversationChain(
    llm=groq_chat,
    memory=memory
)

# Submit Button
submit_button = st.button(label='Ask Question ❓')

if submit_button and user_question:
    with st.spinner('Thinking... 🤔'):
        response = conversation.run(user_question)  # ✅ Fix: Response is a string
        message = {'human': user_question, 'AI': response}

        # Append to Chat History
        st.session_state.chat_history.append(message)

        # Display Chatbot Response
        st.write("Chatbot 🤖:", response)  # ✅ Fix: Removed ['response']

