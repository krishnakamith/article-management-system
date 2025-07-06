from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Article
from django.views.generic import CreateView

def home(request):
    articles = Article.objects.all()
    return render(request, "articles/home.html", {"articles" : articles})

class CreateArticleView(CreateView):
    template_name = "articles/create_article.html"
    model = Article
    fields = ("title", "content", "status", "word_count", "twitter_post")
    success_url = reverse_lazy("home")