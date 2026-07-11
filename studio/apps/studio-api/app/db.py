import os
from datetime import datetime, timezone

from sqlalchemy import DateTime, Integer, String, Text, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL", "").strip()

_engine = None
SessionLocal = None
_MEMORY: list[dict] = []


class Base(DeclarativeBase):
    pass


class Lead(Base):
    __tablename__ = "leads"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(120))
    email: Mapped[str] = mapped_column(String(255))
    message: Mapped[str] = mapped_column(Text)
    project_interest: Mapped[str | None] = mapped_column(String(200), nullable=True)
    received_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))


def using_postgres() -> bool:
    return bool(DATABASE_URL)


def init_db() -> None:
    global _engine, SessionLocal
    if not using_postgres():
        return
    _engine = create_engine(DATABASE_URL, pool_pre_ping=True)
    SessionLocal = sessionmaker(bind=_engine, autoflush=False, autocommit=False)
    Base.metadata.create_all(bind=_engine)


def save_lead(
    name: str,
    email: str,
    message: str,
    project_interest: str | None = None,
) -> dict:
    received_at = datetime.now(timezone.utc)
    record = {
        "name": name,
        "email": email,
        "message": message,
        "project_interest": project_interest,
        "received_at": received_at.isoformat(),
    }
    if using_postgres() and SessionLocal is not None:
        with SessionLocal() as session:
            row = Lead(
                name=name,
                email=email,
                message=message,
                project_interest=project_interest,
                received_at=received_at,
            )
            session.add(row)
            session.commit()
            record["id"] = row.id
        return record
    _MEMORY.append(record)
    return record


def list_leads() -> list[dict]:
    if using_postgres() and SessionLocal is not None:
        with SessionLocal() as session:
            rows = session.query(Lead).order_by(Lead.id.desc()).all()
            return [
                {
                    "id": r.id,
                    "name": r.name,
                    "email": r.email,
                    "message": r.message,
                    "project_interest": r.project_interest,
                    "received_at": r.received_at.isoformat(),
                }
                for r in rows
            ]
    return list(_MEMORY)
