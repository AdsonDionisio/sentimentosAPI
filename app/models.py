from sqlmodel import SQLModel, Field
from pydantic import BaseModel

class InputMessage(BaseModel):
    text: str

class Message(SQLModel, table=True):
    __tablename__ = "messages"

    id: int | None = Field(default=None, primary_key=True)
    text: str
    sentiment: str