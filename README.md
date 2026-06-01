# 🧠 Agentic AI Fake News Detection System

An intelligent Fake News Detection application built using Machine Learning, Agentic AI architecture, and Google Gemini AI.

The system analyzes news articles, predicts whether they are REAL or FAKE, provides credibility analysis, explains the prediction, and generates similar fake news reports using Gemini AI.

---

## 🚀 Features

### 🔍 Fake News Classification
- Uses TF-IDF Vectorization
- Logistic Regression classifier
- Confidence score for predictions

### 📊 Credibility Analysis
- Evaluates trustworthiness of the news content
- Provides credibility notes

### 💡 Explainable AI
- Generates human-readable explanations
- Helps users understand prediction reasoning

### 🤖 Gemini AI Integration
- Generates similar fake news reports
- Useful for pattern analysis and research

### 🌐 Interactive Web Interface
- Built with Streamlit
- Simple and user-friendly interface

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Scikit-Learn
- Pandas
- NumPy
- Google Gemini AI
- Python Dotenv

---

## 📂 Project Structure

```text
project/
│
├── app.py
├── train_model.py
├── fake_news.csv
├── requirements.txt
├── .env
│
├── agents/
│   ├── classifier_agent.py
│   ├── credibility_agent.py
│   ├── explanation_agent.py
│   └── gemini_similarity_agent.py
│
├── model/
│   ├── fake_news_model.pkl
│   ├── tfidf_vectorizer.pkl
│   ├── news_vectors.pkl
│   └── news_dataset.pkl
│
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/fake-news-detection.git
cd fake-news-detection
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Gemini API Key

Create a `.env` file:

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

---

## 🏋️ Train the Model

```bash
python train_model.py
```

This will generate:

- fake_news_model.pkl
- tfidf_vectorizer.pkl
- news_vectors.pkl
- news_dataset.pkl

---

## ▶️ Run Application

```bash
streamlit run app.py
```

---

## Example Workflow

1. Enter a news article.
2. Click Analyze News.
3. System predicts:
   - REAL NEWS
   - FAKE NEWS
4. Displays confidence score.
5. Provides explanation.
6. Generates similar fake reports using Gemini AI.

---

## Future Improvements

- Real-time fact-checking APIs
- News source verification
- Multi-language support
- Deep Learning models (BERT, RoBERTa)
- Web scraping for live news analysis

---

## Author

K. Mohan Koushik

B.Tech Student
Gayatri Vidya Parishad College of Engineering
