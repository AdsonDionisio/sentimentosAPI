from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.database import get_session
from app.models import Message, InputMessage


router = APIRouter(prefix="/message", tags=["Messages"])



@router.get("/")
def read_message( session: Session = Depends(get_session)):
    messages = session.exec(select(Message)).all()    
    return messages


@router.get("/{message_id}")
def read_message(message_id: int, session: Session = Depends (get_session)):
    message = session.get(Message, message_id)
    if not message:
        raise HTTPException(status_code=404, detail="Message not found")
    return message
    

@router.post("/")
def create_message(input_message: InputMessage, 
                    session: Session = Depends (get_session)):
    message = Message(text=input_message.text, sentiment="POS")
    session.add(message)
    session.commit()
    session.refresh(message)

    return message

