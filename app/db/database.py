from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

from app.db.models import Base
from app.settings.config import DB_URL

engine = create_engine(DB_URL)
session_maker = sessionmaker(bind=engine)



class Test(Base):
    __tablename__ ="test"
    id = Column(Integer, primary_key=True, autoincrement=True)




