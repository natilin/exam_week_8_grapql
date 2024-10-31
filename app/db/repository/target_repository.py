from sqlalchemy import func

from app.db.database import session_maker
from app.db.models import Targets


def create_target(new_target: Targets):
    new_target.target_id = get_max_id() + 1
    with session_maker() as session:
        session.add(new_target)
        session.commit()
        session.refresh(new_target)
        return new_target

def get_max_id():
    with session_maker() as session:
        return session.query(func.max(Targets.target_id)).scalar()