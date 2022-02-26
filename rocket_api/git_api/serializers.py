from rest_framework import serializers
from .models import Repositories, UsersName


class RepositoriesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Repositories
        exclude = ('id',)


class UsersNameSerializers(serializers.ModelSerializer):
    class Meta:
        model = UsersName
        exclude = ('id', "repositories_link")


class UsersRepositoriesSerializers(serializers.ModelSerializer):
    repositories_link = serializers.SlugRelatedField(slug_field='repository_name', read_only=True, many=True)

    class Meta:
        model = UsersName
        fields = ('name', 'repositories_link')

