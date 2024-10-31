from tokenize import String

from graphene import ObjectType, List, Field, Int, Date, String

from app.db.repository.mission_repository import find_mission_by_id, find_missions_by_date_range, \
    find_missions_by_country, find_missions_by_industry
from app.gql.types.mission_type import MissionType
from app.gql.types.target_type import TargetType


class Query(ObjectType):
    mission_by_id = Field(MissionType, mission_id=Int())
    mission_by_dates = List(MissionType, start_date=Date(), end_date=Date())
    mission_by_country = List(MissionType, country=String())
    mission_by_industry = List(MissionType, industry=String())


    @staticmethod
    def resolve_mission_by_id(root, info, mission_id):
        res =  find_mission_by_id(mission_id)
        return res


    @staticmethod
    def resolve_mission_by_dates(root, info, start_date, end_date):
        res =  find_missions_by_date_range(start_date, end_date)
        return res

    @staticmethod
    def resolve_mission_by_country(root, info, country):
        res = find_missions_by_country(country)
        return res


    @staticmethod
    def resolve_mission_by_industry(root, info, industry):
        res = find_missions_by_industry(industry)
        return res




