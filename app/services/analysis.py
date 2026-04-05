from transformers import pipeline
from fastapi import Request

def get_sentiment_service(request: Request):
    return request.app.state.analyser

class AnalyserService:
    def __init__(self):
        self.model = pipeline(
            "sentiment-analysis",
            model="pysentimiento/bertweet-pt-sentiment"
        )

    def analyze_sentiment(self, text: str):
        return self.model(text)

