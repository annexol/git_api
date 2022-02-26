from django.db import models



# Create your models here.
class UsersName(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    repositories_link = models.ManyToManyField('Repositories')

    def __str__(self):
        return self.name


class Repositories(models.Model):
    repository_name = models.CharField(max_length=255)
    about = models.CharField(max_length=255, null=True, blank=True)
    site = models.CharField(max_length=127, null=True, blank=True)
    stars = models.IntegerField(null=True, blank=True)
    forks = models.IntegerField(null=True, blank=True)
    watchers = models.IntegerField(null=True, blank=True)
    commits_number = models.IntegerField(null=True, blank=True)
    release_version = models.CharField(max_length=255, null=True, blank=True)
    release_date = models.DateTimeField(null=True, blank=True)
    release_changelog = models.TextField(null=True, blank=True)
    commit_author = models.CharField(max_length=255, null=True, blank=True)
    commit_name = models.CharField(max_length=255, null=True, blank=True)
    commit_date = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.repository_name
