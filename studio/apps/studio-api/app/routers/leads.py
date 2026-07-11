from fastapi import APIRouter
from pydantic import BaseModel, EmailStr, Field

from app.db import list_leads, save_lead

router = APIRouter(tags=["leads"])


class LeadIn(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    email: EmailStr
    message: str = Field(min_length=1, max_length=2000)
    project_interest: str | None = Field(default=None, max_length=200)


@router.post("/leads")
def create_lead(payload: LeadIn):
    record = save_lead(
        payload.name,
        payload.email,
        payload.message,
        payload.project_interest,
    )
    return {"ok": True, "lead": record}


@router.get("/leads")
def get_leads():
    leads = list_leads()
    return {"count": len(leads), "leads": leads}
