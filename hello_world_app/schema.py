from .models import GraphWithUser
from graphene_django import DjangoObjectType
import graphene


class GraphType(DjangoObjectType):
    class Meta:
        model = GraphWithUser
        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
    Graphs = graphene.List(GraphType)

    def resolve_Graphs(self, info):
        return GraphWithUser.objects.filter(user=info.context.user)


schema = graphene.Schema(query=Query)
