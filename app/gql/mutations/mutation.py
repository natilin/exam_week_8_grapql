from graphene import ObjectType

from app.gql.mutations.mission_mutations import CreateMission
from app.gql.mutations.target_mutations import CreateTarget


class Mutation(ObjectType):
    create_mission = CreateMission.Field()
    create_target = CreateTarget.Field()