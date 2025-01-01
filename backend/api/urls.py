from django.contrib import admin
from django.urls import path, include

from .views import ArticleList, ArticleDeatil, UserList, UserDetail

app_name = "api"

urlpatterns = [
    path("", ArticleList.as_view(), name="list"),
    path("<int:pk>", ArticleDeatil.as_view(), name="detail"),
    path("users/", UserList.as_view(), name="user_list"),
    path("users/<int:pk>", UserDetail.as_view(), name="user_detail"),
]
