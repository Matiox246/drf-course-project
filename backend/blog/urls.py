from django.contrib import admin
from django.urls import path, include

from .views import ArticleList, ArticleDetail, ArticleUpdate, ArticleDestroy

app_name = "blog"

urlpatterns = [
    path('', ArticleList.as_view(), name="list"),
    path('<int:pk>', ArticleDetail.as_view(), name="detail"),
    path('<int:pk>/update', ArticleUpdate.as_view(), name="update"),
    path('<int:pk>/destroy', ArticleDestroy.as_view(), name="destroy"),
]
