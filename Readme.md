
# SentiBot 🤖💙  
A lightweight AI-powered chatbot combined with a custom-trained sentiment analysis model.  
Built using **Python**, **Streamlit**, **HuggingFace Transformers**, and **Scikit-Learn**.

---

## 🚀 Features
- Conversational chatbot powered by a free HuggingFace model  
- Custom-trained sentiment classifier (Positive / Negative)  
- Clean and minimal Streamlit UI  
- Chat history saving + download feature  
- 100% Python — no frontend frameworks needed  

---

## 🛠️ Tech Stack
- **HuggingFace Transformers**
- **PyTorch / CPU**
- **Scikit-Learn**
- **NLTK**
- **Streamlit**

---

## 📂 Project Structure
```
SentiBot/
│── app.py               # Streamlit app  
│── chatbot.py           # Chatbot model  
│── sentiment.py         # Sentiment classifier  
│── model.pkl            # Trained sentiment model  
│── vectorizer.pkl       # TF-IDF or CountVectorizer  
│── README.md
│── requirements.txt
```

---

## ▶️ How to Run

### **1. Clone the repository**
```bash
git clone https://github.com/yourusername/SentiBot.git
cd SentiBot
```

### **2. Create virtual environment (recommended)**
```bash
python -m venv env
```

#### **Activate it:**

**Windows**
```bash
env\Scripts\activate
```

**Mac / Linux**
```bash
source env/bin/activate
```

---

### **3. Install dependencies**
```bash
pip install -r requirements.txt
```

---

### **4. Run the Streamlit application**
```bash
streamlit run app.py
```

---

### **5. Open in browser**
Once Streamlit starts, it will show something like:

```
Local URL: http://localhost:8501
```

Open this link to use **SentiBot 🤖💙**

---

## 📦 Dataset  
This project uses the **Amazon Fine Food Reviews** dataset:  
Kaggle → https://www.kaggle.com/datasets/mdraselsarker/amazon-fine-food-reviews

---

## ⚙️ Sentiment Model  
Training includes:
- Text preprocessing  
- TF-IDF Vectorizer  
- Logistic Regression classifier  

The model outputs:  
- **Positive**  
- **Negative**

---

## 📜 License  
This project is licensed under the MIT License.

---

## ✨ Author  
Made with ❤️ for portfolio and production usage.
