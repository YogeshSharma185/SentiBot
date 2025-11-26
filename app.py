import streamlit as st
from chatbot import generate_bot_reply
from sentiment import predict_sentiment
import datetime
# STREAMLIT PAGE CONFIG
st.set_page_config(
    page_title="AI Chatbot with Sentiment Analysis",
    layout="centered",
)
st.markdown("""
    <div style="
        background: linear-gradient(90deg, #1E3A8A, #3B82F6);
        padding: 25px;
        border-radius: 15px;
        margin-bottom: 20px;
        text-align: center;
        color: white;">
        <h1 style="font-size: 42px; margin: 0;">SentiBot 🤖💙</h1>
        <p style="font-size: 18px; margin-top: 8px;">Your Personal AI Chatbot with Sentiment Insights</p>
    </div>
""", unsafe_allow_html=True)
# SESSION STATE FOR CHAT HISTORY
if 'history' not in st.session_state:
    st.session_state.history = []
# USER INPUT
user_input = st.text_input("Type your message:", "")
if st.button("Send") and user_input.strip() != "": 
    # 1. Get sentiment
    sentiment = predict_sentiment(user_input)
    # 2. Generate chatbot reply
    bot_reply = generate_bot_reply(user_input)
    # 3. Save in chat history
    st.session_state.history.append({
        "user": user_input,
        "sentiment": sentiment,
        "bot": bot_reply
    })
# DISPLAY CHAT HISTORY
st.markdown("<hr>", unsafe_allow_html=True)
chat_text = ""    # This will store all chat as text for download
for chat in st.session_state.history:  
    # For download
    chat_text += f"User: {chat['user']}\n"
    chat_text += f"Sentiment: {chat['sentiment']}\n"
    chat_text += f"Bot: {chat['bot']}\n\n"
    # UI display
    st.markdown(f"""
        <div style="background:#E0E7FF;padding:10px;border-radius:10px;margin-bottom:5px;">
            <strong>You:</strong> {chat['user']}
            <br><span style='color:gray;'>Sentiment: <b>{chat['sentiment'].upper()}</b></span>
        </div>
    """, unsafe_allow_html=True)
    st.markdown(f"""
        <div style="background:#F3F4F6;padding:10px;border-radius:10px;margin-bottom:15px;">
            <strong>Bot:</strong> {chat['bot']}
        </div>
    """, unsafe_allow_html=True)
# 📥 DOWNLOAD CHAT BUTTON
if st.session_state.history:
    file_name = f"chat_history_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    st.download_button(
        label="📥 Download Chat History",
        data=chat_text,
        file_name=file_name,
        mime="text/plain"
    )
