from rest_framework import routers
from .api import RepositoriesViewSet, UserNameViewSet
from . import views
from .yasg import urlpatterns as doc_urls
from django.urls import path

urlpatterns = [
    path('api/users', views.UserNameView.as_view()),
    path('api/repositories', views.RepositoriesView.as_view(),name='repository'),
    path('api/user/<slug:name>', views.UserRepositoriesView.as_view()),
    path('api/common_static', views.CommonStaticView.as_view(), name='common_statistic'),
    path('api/detail/<slug:name>', views.UserDetailView.as_view(), name='user_detail'),

]
urlpatterns += doc_urls
