# schema = ...

import graphene

from webapp.chat import schema


class Mutation(schema.Mutation, graphene.ObjectType):
    pass


class Query(schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
