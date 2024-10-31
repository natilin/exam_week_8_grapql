from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError

from app.db.database import session_maker
from app.db.models import Targets, Missions
from app.db.repository.mission_repository import find_mission_by_id


def create_target(new_target: Targets):
    new_target.target_id = get_max_id() + 1
    with session_maker() as session:
        if find_mission_by_id(new_target.mission_id) is not None:
            session.add(new_target)
            session.commit()
            session.refresh(new_target)
            return new_target
        else:
            raise SQLAlchemyError("mission_id doesn't exist")

def get_max_id():
    with session_maker() as session:
        return session.query(func.max(Targets.target_id)).scalar()