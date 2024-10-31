from graphene import ObjectType, List


class Query(ObjectType):
    users = List(UserType)
    cards = List(CardType)
    address = List(AddressType)