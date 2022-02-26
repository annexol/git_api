from django.contrib import admin
from .models import Repositories, UsersName


# Register your models here.

class RepositoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'repository_name')
    search_fields = ('id', 'repository_name')
    list_display_links = ('id', 'repository_name')
    list_filter = ('id', 'repository_name')


class UserNameAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')
    list_display_links = ('id', 'name')
    list_filter = ('id', 'name')



admin.site.register(Repositories, RepositoriesAdmin)
admin.site.register(UsersName, UserNameAdmin)

