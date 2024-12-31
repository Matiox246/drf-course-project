from rest_framework import serializers
from django.contrib.auth.models import User
from blog.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # fields = ("title", "slug", "author", "content", "publish", "status")
        # exclude = ("created", "updated")
        fields = "__all__"
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        
