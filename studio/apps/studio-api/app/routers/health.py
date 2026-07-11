from fastapi import APIRouter

from app.db import using_postgres

router = APIRouter(tags=["health"])


@router.get("/health")
def health():
    return {
        "status": "ok",
        "service": "studio-api",
        "storage": "postgres" if using_postgres() else "memory",
    }
