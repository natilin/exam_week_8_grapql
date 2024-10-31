from sqlalchemy import func

from app.db.database import session_maker
from app.db.models import Missions, Cities, Countries, Targets, TargetTypes

def get_max_id():
    with session_maker() as session:
        return session.query(func.max(Missions.mission_id)).scalar()


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


def create_mission(new_mission: Missions):
    new_mission.mission_id = get_max_id() + 1
    with session_maker() as session:
        session.add(new_mission)
        session.commit()
        session.refresh(new_mission)
        return new_mission


def update_mission_result(mission: Missions):
    with session_maker() as session:

        mission_to_update = session.query(Missions).get(mission.mission_id)
        mission_to_update.aircraft_returned = mission.aircraft_returned
        mission_to_update.aircraft_failed = mission.aircraft_failed
        mission_to_update.aircraft_damaged = mission.aircraft_damaged
        mission_to_update.aircraft_lost = mission.aircraft_lost
        session.commit()
        session.refresh(mission_to_update)
        return mission_to_update


def delete_mission_by_id(m_id):
    with session_maker() as session:
        mission = find_mission_by_id(m_id)
        session.delete(mission)
        session.commit()
        return mission




