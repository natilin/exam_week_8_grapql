from app.db.database import session_maker
from app.db.models import Missions, Cities, Countries, Targets, TargetTypes


def find_mission_by_id(m_id: int) -> Missions:
    with session_maker() as session:
        return session.query(Missions).filter(m_id == Missions.mission_id).first()


def find_missions_by_date_range(start_date, end_date):
    with session_maker() as session:
        return session.query(Missions).filter(Missions.mission_date.between(start_date, end_date)).all()


def find_missions_by_country(country):
    with session_maker() as session:
        return (session.query(Missions)
                .join(Targets)
                .join(Cities)
                .join(Countries)
                .filter(Countries.country_name == country)
                .all())


def find_missions_by_industry(industry):
    with session_maker() as session:
        return (session.query(Missions)
                .join(Targets)
                .filter(Targets.target_industry == industry)
                .all())


def find_missions_by_target_type(type):
    with session_maker() as session:
        return (session.query(Missions)
                .join(Targets)
                .join(TargetTypes)
                .filter(TargetTypes.target_type_name == type)
                .all())




