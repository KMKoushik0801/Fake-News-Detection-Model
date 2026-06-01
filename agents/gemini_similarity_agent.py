import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

class GeminiSimilarityAgent:

    def __init__(self):
        api_key = os.getenv("GOOGLE_API_KEY")

        if not api_key:
            raise ValueError("Google API key not found.")

        self.client = genai.Client(api_key=api_key)

    def get_similar_news(self, input_text):

        prompt = f"""
        The following news article was classified as FAKE NEWS:

        "{input_text}"

        Instead of generating fake content, provide 3 summaries of
        similar real-world news topics that have been reported in the past.

        Guidelines:
        - Only describe factual, realistic events.
        - Do not invent sensational claims.
        - Keep each summary 3-4 sentences.
        - Focus on legitimate news themes similar to the topic.
        """

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text
