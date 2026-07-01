# 🛡️ Arabic Hateful Speech Detector

An end-to-end Natural Language Processing (NLP) web application that automatically detects hateful and abusive Arabic text using Machine Learning.

The system preprocesses Arabic text, extracts linguistic features using TF-IDF vectorization, and classifies user input with a Logistic Regression model, delivering real-time predictions through an interactive Streamlit interface.

---

## 🚀 Live Demo

👉 **Try the application here:**

https://hatful-speech-detector.streamlit.app/

---

## ✨ Project Highlights

- Arabic text preprocessing pipeline
- Arabic stopword removal
- Arabic text normalization
- Character-level TF-IDF feature extraction
- Logistic Regression classifier
- Real-time sentiment prediction
- Prediction confidence scores
- Interactive Streamlit web application
- Deployable production-ready model using Joblib

---

## 🗂 Dataset

**Arabic Sentiment Analysis Dataset (SS2030)**

The dataset contains labeled Arabic social media posts used to train a binary sentiment classifier.

---

## 🧠 Machine Learning Pipeline

```text
Raw Arabic Text
       │
       ▼
Text Cleaning
       │
       ▼
Arabic Normalization
       │
       ▼
Stopword Removal
       │
       ▼
Character-level TF-IDF Vectorization
       │
       ▼
Logistic Regression Classifier
       │
       ▼
Prediction + Confidence Score
```

---

# 📈 Model Performance

### Classification Metrics

<img width="699" height="453" alt="Performance Metrics" src="https://github.com/user-attachments/assets/79af5150-8049-4e0a-b6b5-1e8be6e8f9fb" />

The model achieves strong performance across all evaluation metrics, demonstrating reliable classification of Arabic social media posts.

---

### ROC Curve

<img width="448" height="455" alt="ROC Curve" src="https://github.com/user-attachments/assets/cca6d46f-2ce8-4ff9-887e-82135f747ca6" />

The Receiver Operating Characteristic (ROC) curve illustrates the model's ability to distinguish between positive and negative classes across different decision thresholds. A larger Area Under the Curve (AUC) indicates better overall classification performance.

---

### Confusion Matrix

<img width="507" height="438" alt="Confusion Matrix" src="https://github.com/user-attachments/assets/928ab6a6-f23c-4873-91b5-6db36a3400cb" />

The confusion matrix summarizes prediction outcomes by comparing actual labels with predicted labels, providing insight into true positives, true negatives, false positives, and false negatives.

---

# 🛠 Technologies

- Python
- Scikit-learn
- Streamlit
- Pandas
- NumPy
- NLTK
- Joblib
- TF-IDF Vectorization

---

# 📊 Performance

| Metric | Score |
|---------|------:|
| Accuracy | **87%** |
| Precision |  **89%** |
| Recall |  **89%** |
| F1 Score |  **89%** |

---

# ⚙️ Installation

```bash
git clone https://github.com/karemramdan0/hatful-speech-detector.git

cd hatful-speech-detector

pip install -r requirements.txt

streamlit run app.py
```

---

# 👨‍💻 Author

**Karem Ramadan**

Machine Learning | Data Science | Artificial Intelligence

If you found this project interesting, consider giving it a ⭐ on GitHub.
