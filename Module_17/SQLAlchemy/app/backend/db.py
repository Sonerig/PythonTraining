from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine("sqlite:///taskmanager.db")
SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass