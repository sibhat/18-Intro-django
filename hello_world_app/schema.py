from .models import GraphWithUser
from graphene_django import DjangoObjectType

import graphene


class GraphType(DjangoObjectType):
    class Meta:
        model = GraphWithUser
        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
    Graph = graphene.List(GraphType, title=graphene.String(), content=graphene.String())

    def resolve_Graph(self, info, title=None, content=None):
        user = info.context.user
        if user.is_anonymous:
            return GraphWithUser.objects.none()
        else:
            if title is not None:
                return GraphWithUser.objects.filter(user=user, title=title)
            elif content is not None:
                return GraphWithUser.objects.filter(user=user, content=content)
            else:
                return GraphWithUser.objects.filter(user=user)


class CreateGraphWithUser(graphene.Mutation):
    graph = graphene.Field(GraphType)
    ok = graphene.Boolean()
    status = graphene.String()

    class Arguments:
        title = graphene.String()
        content = graphene.String()

    def mutate(self, info, title, content):
        user = info.context.user
        if user.is_anonymous:
            return CreateGraphWithUser(ok=False, status="Must be logged in!")
        else:
            new_graph = GraphWithUser(title=title, content=content, user=user)
            new_graph.save()
            return CreateGraphWithUser(graph=new_graph, ok=True, status="ok")


class Mutation(graphene.ObjectType):
    create_graphWithUser = CreateGraphWithUser.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
