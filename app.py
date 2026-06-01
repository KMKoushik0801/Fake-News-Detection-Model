import streamlit as st
from agents.classifier_agent import ClassifierAgent
from agents.credibility_agent import CredibilityAgent
from agents.explanation_agent import ExplanationAgent
from agents.gemini_similarity_agent import GeminiSimilarityAgent


# -----------------------------
# Initialize Agents
# -----------------------------
classifier = ClassifierAgent()
credibility = CredibilityAgent()
explainer = ExplanationAgent()
gemini_agent = GeminiSimilarityAgent()


# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Agentic AI Fake News Detection", layout="wide")

st.title("🧠 Agentic AI - Fake News Detection System")

st.write("Enter a news article below to analyze whether it is Real or Fake.")

news_input = st.text_area("📰 Enter News Content:", height=200)

if st.button("Analyze News"):

    if news_input.strip() == "":
        st.warning("Please enter some news text.")
    else:
        # -----------------------------
        # Classification
        # -----------------------------
        label, confidence = classifier.classify(news_input)

        credibility_note = credibility.analyze(news_input)

        explanation = explainer.explain(label, credibility_note, confidence)

        # -----------------------------
        # Show Result
        # -----------------------------
        if label == "REAL NEWS":
            st.success(label)
        else:
            st.error(label)

        st.info(f"Confidence: {confidence}%")

        st.subheader("📌 Explanation")
        st.write(explanation)

        # -----------------------------
        # Gemini Similar News (Only if Fake)
        # -----------------------------
        if label == "FAKE NEWS":
            st.subheader("🤖 AI Generated Similar Fake News Reports")

            with st.spinner("Generating similar reports using Gemini AI..."):
                try:
                    similar_reports = gemini_agent.get_similar_news(news_input)
                    st.write(similar_reports)

                except Exception as e:
                    st.error("Error generating similar news reports.")
                    st.write(str(e))
