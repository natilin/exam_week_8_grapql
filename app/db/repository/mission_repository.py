from app.db.database import session_maker
from app.db.models import Missions


def find_mission_by_id(m_id: int) -> Missions:
    with session_maker() as session:
        return session.query(Missions).filter(m_id == Missions.mission_id).first()


def find_missions_by_date_range(start_date, end_date):
    with session_maker() as session:
        return session.query(Missions).filter(Missions.mission_date.between(start_date, end_date)).all()




