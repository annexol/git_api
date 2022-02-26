from django.shortcuts import render
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UsersName, Repositories
from .serializers import *
from django.db import models
from django.db.models import Avg, Max, Min, Sum


# Create your views here.
# from rest_framework.viewsets import ModelViewSet


class UserNameView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        users = UsersName.objects.all()
        serializer = UsersNameSerializers(users, many=True)
        return Response(serializer.data)


class RepositoriesView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        repositories = Repositories.objects.all()
        serializer = RepositoriesSerializers(repositories, many=True)
        return Response(serializer.data)


class UserRepositoriesView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, name):
        users = UsersName.objects.get(name=name)
        serializer = UsersRepositoriesSerializers(users)
        return Response(serializer.data)


class CommonStaticView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        users = UsersName.objects.all().annotate(
            count_repositories=models.Count('repositories_link')
        )

        count_users = len(users)
        count_repositories = 0
        for count in users:
            count_repositories += count.count_repositories
        middle_repository = round(count_repositories / count_users, 2)
        # print(users[1].repositories_link.all())
        return Response({'count_users': count_users, 'count_repositories': count_repositories,
                         'middle_count_repository': middle_repository})


class UserDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, name):
        user = UsersName.objects.get(name=name)
        repositories = user.repositories_link.all()
        max_commit = repositories.aggregate(Max('commits_number'))
        repository = repositories.filter(commits_number=max_commit['commits_number__max'])[0]
        avg_stars = repositories.aggregate(Avg('stars'))
        return Response({'user': user.name, repository.repository_name: repository.commits_number,
                         'avg_stars': avg_stars["stars__avg"]})
