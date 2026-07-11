from fastapi import APIRouter
from pydantic import BaseModel, EmailStr, Field

from app.db import list_messages, save_message

router = APIRouter(tags=["contact"])


class ContactIn(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    email: EmailStr
    message: str = Field(min_length=1, max_length=2000)


@router.post("/contact")
def contact(payload: ContactIn):
    save_message(payload.name, payload.email, payload.message)
    return {"ok": True, "message": "Thanks — we received your note."}


@router.get("/contact")
def list_contact():
    messages = list_messages()
    return {"count": len(messages), "messages": messages}
