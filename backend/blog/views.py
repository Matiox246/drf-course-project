from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import Article
# Create your views here.


class ArticleList(ListView):
    def get_queryset(self):
        return Article.objects.filter(status=True)
    template_name = "blog/article_list.html"
    
class ArticleDetail(DetailView):
    def get_object(self):
        return get_object_or_404(
            Article.objects.filter(status=True),
            pk=self.kwargs.get("pk"))
    

class ArticleUpdate(UpdateView):
    fields = "__all__"
    def get_object(self):
        return get_object_or_404(
            Article.objects.filter(status=True),
            pk=self.kwargs.get("pk"))
    

class ArticleDestroy(DeleteView):
    success_url = "/"
    def get_object(self):
        return get_object_or_404(
            Article.objects.filter(status=True),
            pk=self.kwargs.get("pk"))