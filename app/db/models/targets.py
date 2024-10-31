from sqlalchemy import Column, Integer, String, Date, Float

from app.db.models import Base


class Targets(Base):
    __tablename__ ="targets"
    mission_id = Column(Integer, primary_key=True, autoincrement=True)
    mission_date = Column(Date)
    airborne_aircraft = Column(Float)
    attacking_aircraft = Column(Float)
    attacking_aircraft = Column(Float)