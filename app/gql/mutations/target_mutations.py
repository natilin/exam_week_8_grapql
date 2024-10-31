from graphene import Mutation, Int, String, Float, Field

from app.db.models import Targets
from app.db.repository.target_repository import create_target
from app.gql.types.target_type import TargetType


class CreateTarget(Mutation):
    class Arguments:
        mission_id = Int()
        target_industry = String()
        city_id = Int()
        target_type_id = Int()
        target_priority = Int()

    target = Field(TargetType)


    @staticmethod
    def mutate(root, info, mission_id, target_industry, city_id, target_type_id, target_priority):
        new_target = Targets(mission_id=mission_id,
                             target_industry=target_industry,
                             city_id=city_id,
                             target_type_id=target_type_id,
                             target_priority=target_priority
                             )
        inserted_target =  create_target(new_target)
        return CreateTarget(target=inserted_target)
