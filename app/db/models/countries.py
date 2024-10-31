from sqlalchemy import Column, Integer, String, ForeignKey

from app.db.models import Base


class Countries(Base):
    __tablename__ ="countries"
    country_id = Column(Integer, primary_key=True, autoincrement=True)
    country_name = Column(String)
