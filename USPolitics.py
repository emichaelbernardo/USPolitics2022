import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS
import numpy as np

#title
st.title('Tweet Sentiment Analysis')
#markdown
st.markdown('This application will perform sentiment analysis on tweets from Senators and Congressmen/women leading to the 2022 US Midterm Elections.')
#sidebar
st.sidebar.title('Sentiment Analysis of Congress Tweets')
# sidebar markdown 
st.sidebar.markdown("🛫We analyse Congress Tweets using this application.🛫")
#loading the data (the csv file is in the same folder)
#if the file is stored the copy the path and paste in read_csv method.
data=pd.read_csv('data/all_tweets_clean.csv')
#checkbox to show data 
if st.checkbox("Show Data"):
    st.write(data.head(50))
#subheader
st.sidebar.subheader('Tweets Analyser')