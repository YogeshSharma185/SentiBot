import pickle
import re
import string
import nltk
from nltk.corpus import stopwords
# Download stopwords if running first time
nltk.download('stopwords')
STOPWORDS = set(stopwords.words('english'))
# Load saved model & vectorizer
model = pickle.load(open("sentiment_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
# TEXT CLEANING FUNCTION
def clean_text(text):
    text = text.lower()                                    # lowercase
    text = re.sub(r"http\S+|www\S+", "", text)             # remove links
    text = re.sub(r"[^a-zA-Z ]", "", text)                 # remove non letters
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = " ".join([word for word in text.split() if word not in STOPWORDS])
    return text
# SENTIMENT PREDICT FUNCTION
def predict_sentiment(text):
    cleaned = clean_text(text)
    vector = vectorizer.transform([cleaned])
    result = model.predict(vector)[0]
    return result
