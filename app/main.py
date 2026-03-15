from fastapi import FastAPI, Response, status
from .model import Message
from .analysis import analyze_sentiment, get_result

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/message/{message_id}")
def read_message(message_id: int):
    return get_result()

@app.post("/message")
def create_message(message: Message):
    analyze_sentiment(message.text)
    return Response(status_code=status.HTTP_200_OK)

