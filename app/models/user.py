from sqlalchemy import String, Integer, DateTime, Column, Boolean
from datetime import datetime, timezone

from app.core.database import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(String(100), unique=True, nullable=False, index=True)
    subscribe = Column(Boolean, default=False)
    date = Column(DateTime)
