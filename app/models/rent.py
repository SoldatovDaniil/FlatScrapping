import sqlalchemy as sa
from sqlalchemy import create_engine, String, Integer, Boolean, DateTime, Text, Numeric, JSON, ForeignKey, Column
from datetime import datetime, timezone

from app.core.database import Base


class Rent(Base):
    __tablename__ = 'rent'

    id = Column(Integer, primary_key=True, autoincrement=True)
    external_id = Column(String(100), unique=True, nullable=False, index=True)
    source = Column(String(50), nullable=False)
    url = Column(Text, nullable=False)
    title = Column(Text, nullable=False)
    adress = Column(Text, nullable=False)
    rent = Column(Text, nullable=False)
    rent_description = Column(Text, nullable=False)
    description = Column(Text)
    data = Column(Text, nullable=False)


    def to_dict(self):
        return {
            "id": self.id,
            "external_id": self.external_id,
            "source": self.source,
            "url": self.url,
            "title": self.title,
            "adress": self.adress,
            "rent": self.rent,
            "rent_description": self.rent_description,
            "description": self.description,
            "data": self.data
        }

