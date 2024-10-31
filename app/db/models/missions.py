from sqlalchemy import Column, Integer, String, Date

from app.db.models import Base


class Missions(Base):
    __tablename__ ="missions"
    mission_id = Column(Integer, primary_key=True, autoincrement=True)
    mission_date = Column(Date)