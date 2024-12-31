from django.contrib import admin
from django.urls import path, include

from .views import ArticleList, ArticleDeatil, UserList, UserDetail, UserUpdate, UserDestroy

app_name = "api"

urlpatterns = [
    path("", ArticleList.as_view(), name="list"),
    path("<int:pk>", ArticleDeatil.as_view(), name="detail"),
    path("users/", UserList.as_view(), name="user_detail"),
    path("users/<int:pk>", UserDetail.as_view(), name="user_detail"),
    path("users/<int:pk>/update", UserUpdate.as_view(), name="user_update"),
    path("users/<int:pk>/destroy", UserDestroy.as_view(), name="user_destroy"),
]
