import streamlit as st
from pathlib import Path
from groq import Groq
from kaggle_secrets import UserSecretsClient

# Load Groq API key
user_secrets = UserSecretsClient()
api_key = user_secrets.get_secret("groq_api")
client = Groq(api_key=api_key)

st.title("Urdu Meeting Summarizer")

# Upload transcript
uploaded_file = st.file_uploader("Upload your full transcript (.txt)", type="txt")

if uploaded_file:
    text = uploaded_file.read().decode("utf-8")
    
    # -------------------------------
    # Generate Summary
    # -------------------------------
    summary_response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": "You are an assistant that creates human-like abstractive summaries in Urdu."},
            {"role": "user", "content": f"Summarize the following Urdu transcript into a clear, concise, well-structured summary:\n\n{text}"}
        ],
        temperature=0.4,
        max_tokens=600
    )
    summary = summary_response.choices[0].message.content

    st.subheader("Summary")
    st.write(summary)

   
