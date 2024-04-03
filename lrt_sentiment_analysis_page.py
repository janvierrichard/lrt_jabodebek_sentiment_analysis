from dotenv import dotenv_values
import streamlit as st
import streamlit.components.v1 as components
from nlp_core.sentiment_analysis import Sentiment_Analysis
import nltk

env = dotenv_values(".env")

def renderPage():
    st.title("LRT Jabodebek Sentiment Analysis")
    components.html("""<hr style="height:3px;border:none;color:#333;background-color:#333; margin-bottom: 10px" /> """)
    st.subheader("Analisis Teks Berdasarkan Input User")
    st.text("Menganalisis data teks yang diberikan user and menentukan sentimennya.")
    st.text("")
    userText = st.text_input('User input', placeholder = 'Input text HERE')
    st.text("")
    if st.button('Predict'):
        if userText != "":
            with st.spinner(text = "Sentiment Prediction is loading..."):
                st.text("")
                sa = Sentiment_Analysis()
                result = sa.predict_sentiment(userText)
                st.text(result)