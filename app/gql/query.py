from graphene import ObjectType, List, Field, Int, Date

from app.db.repository.mission_repository import find_mission_by_id, find_missions_by_date_range
from app.gql.types.mission_type import MissionType
from app.gql.types.target_type import TargetType


class Query(ObjectType):
    mission_by_id = Field(MissionType, mission_id=Int())
    mission_by_dates = List(MissionType, start_date=Date, end_date=Date)


    @staticmethod
    def resolve_mission_by_id(root, info, mission_id):
        res =  find_mission_by_id(mission_id)
        return res


    @staticmethod
    def resolve_mission_by_dates(root, info, start_date, end_date):
        res =  find_missions_by_date_range(start_date, end_date)
        return res