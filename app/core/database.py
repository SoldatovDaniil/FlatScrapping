import os
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class Base(DeclarativeBase):
    pass


engine = create_engine(os.getenv("DATABASE_URL"), echo=False, pool_pre_ping=True)

session_maker = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_db():
    Base.metadata.create_all(bind=engine)


def drop_db():
    Base.metadata.drop_all()