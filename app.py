import streamlit as st
import sidebar
import biodata
import lrt_sentiment_analysis_page
import nltk

page = sidebar.show()

if page == "Biodata":
    biodata.renderPage()
elif page == "LRT Jabodebek Sentiment Analysis":
    lrt_sentiment_analysis_page.renderPage()