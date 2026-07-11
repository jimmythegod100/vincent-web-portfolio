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


class ContactMessage(Base):
    __tablename__ = "contact_messages"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(120))
    email: Mapped[str] = mapped_column(String(255))
    message: Mapped[str] = mapped_column(Text)
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


def save_message(name: str, email: str, message: str) -> dict:
    received_at = datetime.now(timezone.utc)
    record = {
        "name": name,
        "email": email,
        "message": message,
        "received_at": received_at.isoformat(),
    }
    if using_postgres() and SessionLocal is not None:
        with SessionLocal() as session:
            row = ContactMessage(
                name=name,
                email=email,
                message=message,
                received_at=received_at,
            )
            session.add(row)
            session.commit()
            record["id"] = row.id
        return record
    _MEMORY.append(record)
    return record


def list_messages() -> list[dict]:
    if using_postgres() and SessionLocal is not None:
        with SessionLocal() as session:
            rows = session.query(ContactMessage).order_by(ContactMessage.id.desc()).all()
            return [
                {
                    "id": r.id,
                    "name": r.name,
                    "email": r.email,
                    "message": r.message,
                    "received_at": r.received_at.isoformat(),
                }
                for r in rows
            ]
    return list(_MEMORY)
