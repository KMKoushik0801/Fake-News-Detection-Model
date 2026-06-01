import pickle

class ClassifierAgent:

    def __init__(self):
        self.model = pickle.load(open("model/fake_news_model.pkl", "rb"))
        self.vectorizer = pickle.load(open("model/tfidf_vectorizer.pkl", "rb"))

    def classify(self, text):
        vectorized = self.vectorizer.transform([text])
        prediction = self.model.predict(vectorized)[0]
        probability = self.model.predict_proba(vectorized)[0].max()

        label = "REAL NEWS" if prediction == 1 else "FAKE NEWS"
        return label, round(probability * 100, 2)
