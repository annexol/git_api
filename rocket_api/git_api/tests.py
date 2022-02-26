from django.urls import reverse
from rest_framework.test import APITestCase
from .models import *
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import AbstractUser, User


class UserDetailTests(APITestCase):
    def setUp(self):
        self.repositories = Repositories.objects.create(
            repository_name='repository_name_test',
            about='about_test',
            site='site_test',
            stars=22,
            forks=10,
            watchers=100,
            commits_number=15,
            release_version='test_release_version',
            release_date='2022-02-26',
            release_changelog='test_changelog',
            commit_author='test_author',
            commit_name='test_commit_name',
            commit_date='2021-12-07T12:45:17.000+00:00'
        )

        self.users = User.objects.create_user(
            username='test_user_name',
            password='some_password',
        )
        self.username = UsersName.objects.create(
            name='test_username',
            link='test_link',

        )

        self.token = Token.objects.create(user=self.users)

    def test_detail_user(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get(reverse('common_statistic'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
