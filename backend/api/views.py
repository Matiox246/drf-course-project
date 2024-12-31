from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView,UpdateAPIView, DestroyAPIView
from django.shortcuts import render
from django.contrib.auth.models import User

from .serializers import ArticleSerializer, UserSerializer
from blog.models import Article
# Create your views here.

class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDeatil(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # lookup_field = "slug"


class UserList(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdate(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDestroy(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer