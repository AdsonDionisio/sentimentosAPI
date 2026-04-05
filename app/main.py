from fastapi import FastAPI
from sqlmodel import SQLModel
from app.database import engine
from app.routes import analysis
from app.services.analysis import AnalyserService

app = FastAPI()

@app.on_event("startup")
def on_startup():
    app.state.analyser = AnalyserService()
    SQLModel.metadata.create_all(engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(analysis.router)


