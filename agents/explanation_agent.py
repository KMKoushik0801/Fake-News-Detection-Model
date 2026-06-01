class ExplanationAgent:

    def explain(self, label, credibility_note, confidence):
        explanation = f"""
        Prediction: {label}
        Confidence Score: {confidence}%

        Reasoning:
        - NLP classification completed
        - {credibility_note}
        - Model confidence considered
        """

        return explanation
