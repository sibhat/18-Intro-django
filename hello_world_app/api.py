from rest_framework import serializers, viewsets
from .models import GraphWithUser


class GraphWithUserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = GraphWithUser
        fields = ('title', 'content')

    def create(self, validated_data):
        # import pdb; pdb.set_trace()
        user = self.context['request'].user
        graph = GraphWithUser.objects.create(user=user, **validated_data)
        return graph


class GraphWithUserViewSet(viewsets.ModelViewSet):
    serializer_class = GraphWithUserSerializer
    queryset = GraphWithUser.objects.none()

    def get_queryset(self):
        # import pdb; pdb.set_trace()
        user = self.request.user

        if user.is_anonymous:
            return GraphWithUser.objects.none()
        else:
            return GraphWithUser.objects.filter(user=user)
