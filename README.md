# Hatful-Speech-Detector
An NLP binary classifier using Logistic Regression to detect negative sentiment, cyberbullying, and harassment in online posts.

## Live Demo

[https://your-streamlit-app.streamlit.app
](https://hatful-speech-detector.streamlit.app/)
## Features

- Arabic text preprocessing
- Arabic stopword removal
- Character-level TF-IDF
- Logistic Regression classifier
- Real-time predictions
- Confidence score
- Streamlit web interface

## Dataset

Arabic Sentiment Analysis Dataset (SS2030)

## Machine Learning Pipeline

Raw Text
↓
Cleaning
↓
Normalization
↓
TF-IDF Vectorization
↓
Logistic Regression
↓
Prediction

## Technologies

- Python
- Scikit-Learn
- Streamlit
- Pandas
- NLTK
- Joblib

## Results

Accuracy: 96.3%

## Installation

```bash
git clone https://github.com/karemramdan0/hatful-speech-detector.git
cd hatful-speech-detector
pip install -r requirements.txt
streamlit run app.py
