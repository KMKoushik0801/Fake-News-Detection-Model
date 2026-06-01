import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer

# Load dataset
df = pd.read_csv("fake_news.csv")

X = df['text']
y = df['label']

vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
X_vectorized = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized, y, test_size=0.2, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

# Save everything
pickle.dump(model, open("model/fake_news_model.pkl", "wb"))
pickle.dump(vectorizer, open("model/tfidf_vectorizer.pkl", "wb"))
pickle.dump(X_vectorized, open("model/news_vectors.pkl", "wb"))
pickle.dump(df, open("model/news_dataset.pkl", "wb"))

print("Model + similarity data saved!")
