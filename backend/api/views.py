from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView,UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import SessionAuthentication

from django.shortcuts import render
from django.contrib.auth.models import User

from .serializers import ArticleSerializer, UserSerializer
from blog.models import Article
from .permissions import IsAuthorOrReadOnly, IsStaffOrReadOnly, IsSuperUserOrStaffReadOnly
# Create your views here.

class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # permission_classes = (IsStaffOrReadOnly, )
    


class ArticleDeatil(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthorOrReadOnly, )
    # lookup_field = "slug"


class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrStaffReadOnly,)

    
class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrStaffReadOnly,)