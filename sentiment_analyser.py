import streamlit as st
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
# nltk.download('vader_lexicon')

st.title('Sentiment Analyser App')
st.write('This app uses VADER to clasify the sentiment of your input as postive, neutral or negative. It is built on top of streamlit.')

form = st.form(key='sentiment-form')
user_input = form.text_area('Enter your text')
submit = form.form_submit_button('Submit')

if submit:
    sid = SentimentIntensityAnalyzer()
    score = sid.polarity_scores(user_input)['compound']

    if score >= 0.05:
        st.success(f'Positive sentiment (score: {score})')
    elif score <= -0.05:
        st.error(f'Negative sentiment (score: {score})')
    else:
        st.warning(f'Neutral sentiment (score: {score})')
