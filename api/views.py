from .serializers import ProfileSerializer, GroupSerializer
from users_roles.models import Profile, Groups
from rest_framework import generics, viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response


class AllUsers(generics.ListCreateAPIView):
    serializer_class = ProfileSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny, )

    def get_queryset(self):
        return Profile.objects.all()

    def perform_create(self, serializer):
        serializer.save()
        return Response(Profile.token, status=status.HTTP_201_CREATED)


class RetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Profile.objects.all()


class AllGroups(viewsets.ModelViewSet):
    queryset = Groups.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication,)

    def destroy(self, request, *args, **kwargs):
        current_user = request.user
        group = self.get_object()
        if current_user.group_id != group.id:
            group.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_304_NOT_MODIFIED)


