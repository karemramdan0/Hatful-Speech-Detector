
import streamlit as st
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
import joblib

# Download NLTK stopwords if not already downloaded
try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords", quiet=True)

arabic_stopwords = set(stopwords.words("arabic"))

# Define the cleaning function (copied from earlier in the notebook)
def clean_arabic_tweet(text):
    text = re.sub(r'http\S+|www\S+|[a-zA-Z0-9]+|@\S+', '', text)
    text = text.replace("_", " ")
    tashkeel = re.compile(r'[\u0617-\u061A\u064B-\u0652]')
    text = re.sub(tashkeel, '', text)
    text = re.sub(r'[^\u0600-\u06FF\s]', '', text)
    text = re.sub(r'[أإآ]', 'ا', text)
    text = re.sub(r'[ؤ]', 'ء', text)
    text = re.sub(r'[ئ]', 'ء', text)
    text = re.sub(r'[ة]', 'ه', text)
    text = re.sub(r'(.)\1{2,}', r'\1', text)
    text = re.sub(r'\bRT\b', '', text)
    words = text.split()
    cleaned_words = [word for word in words if word not in arabic_stopwords]
    return ' '.join(cleaned_words)

# Load the vectorizer and model
vectorizer = joblib.load('tfidf_vectorizer.joblib')
model = joblib.load('logistic_regression_model.joblib')

# Streamlit App Title
st.title('Arabic Tweet Sentiment Predictor')
st.write('Enter an Arabic tweet below to predict its sentiment (Positive or Negative).')

# Text Area for user input
user_input = st.text_area('Enter your tweet here:', height=150)

# Prediction Button
if st.button('Predict Sentiment'):
    if user_input:
        # Clean the input tweet
        cleaned_input = clean_arabic_tweet(user_input)

        # Transform the cleaned tweet using the loaded vectorizer
        numerical_features = vectorizer.transform([cleaned_input])

        # Get prediction and probabilities
        prediction = model.predict(numerical_features)[0]
        probabilities = model.predict_proba(numerical_features)[0]

        # Display results
        st.write('---')
        st.subheader('Prediction Results:')
        
        sentiment_label = "Positive 😊" if prediction == 1 else "Negative 🤬"
        st.write(f"**Sentiment:** {sentiment_label}")
        st.write(f"**Confidence (Positive):** {probabilities[1]*100:.2f}%")
        st.write(f"**Confidence (Negative):** {probabilities[0]*100:.2f}%")
        
        st.write('---')
        st.write(f"**Original Post:** {user_input}")
        st.write(f"**Cleaned Post:** {cleaned_input}")
    else:
        st.warning('Please enter a tweet to predict sentiment.')
