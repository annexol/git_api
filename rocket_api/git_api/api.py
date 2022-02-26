from .models import Repositories, UsersName
from rest_framework import viewsets, permissions
from .serializers import RepositoriesSerializers, UsersNameSerializers


class RepositoriesViewSet(viewsets.ModelViewSet):
    queryset = Repositories.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RepositoriesSerializers


class UserNameViewSet(viewsets.ModelViewSet):
    queryset = UsersName.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UsersNameSerializers
