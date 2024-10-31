from graphene import Mutation, Int, String, Float, Field

from app.db.models import Missions
from app.db.repository.mission_repository import create_mission, update_mission_result, delete_mission_by_id
from app.gql.types.mission_type import MissionType


class CreateMission(Mutation):
    class Arguments:
        mission_date = String()
        airborne_aircraft = Float()
        attacking_aircraft = Float()
        bombing_aircraft = Float()


    mission = Field(MissionType)

    @staticmethod
    def mutate(root, info,
               mission_date,
               airborne_aircraft,
               attacking_aircraft, bombing_aircraft):

        new_mission = Missions(mission_date=mission_date,
                               airborne_aircraft=airborne_aircraft,
                               attacking_aircraft=attacking_aircraft,
                               bombing_aircraft=bombing_aircraft,

                               )
        inserted_mission =  create_mission(new_mission)
        return CreateMission(mission=inserted_mission)


class UpdateMission(Mutation):
    class Arguments:
        mission_id = Int()
        aircraft_returned = Float()
        aircraft_failed = Float()
        aircraft_damaged = Float()
        aircraft_lost = Float()


    mission = Field(MissionType)

    @staticmethod
    def mutate(root, info, mission_id, aircraft_returned,
               aircraft_failed, aircraft_damaged, aircraft_lost):
        mission_to_update = Missions(mission_id=mission_id,
                                     aircraft_returned=aircraft_returned,
                                     aircraft_failed=aircraft_failed,
                                     aircraft_damaged=aircraft_damaged,
                                     aircraft_lost=aircraft_lost
                                     )
        updated_mission = update_mission_result(mission_to_update)
        return UpdateMission(mission=updated_mission)


class DeleteMission(Mutation):
    class Arguments:
        mission_id = Int()

    mission = Field(MissionType)

    @staticmethod
    def mutate(root, info, mission_id):
        deleted_mission = delete_mission_by_id(mission_id)
        return DeleteMission(mission=deleted_mission)