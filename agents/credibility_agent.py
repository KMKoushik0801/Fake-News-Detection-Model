class CredibilityAgent:

    def analyze(self, text):
        suspicious_words = ["shocking", "breaking", "unbelievable", "secret", "exposed"]

        count = sum(word in text.lower() for word in suspicious_words)

        if count >= 2:
            return "High sensational language detected."
        elif count == 1:
            return "Moderate sensational tone."
        else:
            return "Neutral tone detected."
