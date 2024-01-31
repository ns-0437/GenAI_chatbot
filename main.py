import os

import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai

# Load environment variables
load_dotenv()

# Configure Streamlit page settings for a dark theme using custom CSS
st.set_page_config(
    page_title="Chat with Gemini-Pro!",
    page_icon=":alien:",  # Favicon emoji
    layout="centered",  # Page layout option
)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

# Function to translate roles between Gemini-Pro and Streamlit terminology
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role

# Initialize chat session in Streamlit if not already present
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# Apply dark theme using custom CSS with white background
st.markdown(
    """
    <style>
        body {
            background-color: white;
            color: #333333;
        }
        .st-bq {
            background-color: #f5f5f5 !important;
            color: #333333 !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the chatbot's title on the page with a dark theme and white background
st.markdown('<h1 style="color: #333333;">🤖 Gemini Pro - ChatBot</h1>', unsafe_allow_html=True)

# Display the chat history
for message in st.session_state.chat_session.history:
    role = translate_role_for_streamlit(message.role)
    text = message.parts[0].text

    # Add background color to the assistant's messages with a dark theme and white background
    if role == "assistant":
        text = f'<div style="background-color: #f5f5f5; color: #333333; padding: 10px; border-radius: 5px; margin-bottom: 10px;">{text}</div>'

    with st.chat_message(role):
        st.markdown(text, unsafe_allow_html=True)

# Input field for the user's message
user_prompt = st.chat_input("Ask Gemini-Pro...")

if user_prompt:
    # Add the user's message to the chat and display it
    st.chat_message("user").markdown(user_prompt)

    # Send the user's message to Gemini-Pro and get the response
    gemini_response = st.session_state.chat_session.send_message(user_prompt)

    # Display Gemini-Pro's response with a different background color and dark theme
    with st.chat_message("assistant"):
        st.markdown(
            f'<div style="background-color: #f5f5f5; color: #333333; padding: 10px; border-radius: 5px; margin-bottom: 10px;">{gemini_response.text}</div>',
            unsafe_allow_html=True
        )
