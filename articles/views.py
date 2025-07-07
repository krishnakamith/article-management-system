from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Article
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)

class ArticleListView(ListView):
    template_name = "articles/home.html"
    model = Article
    context_object_name = "articles"

class ArticleCreateView(CreateView):
    template_name = "articles/create_article.html"
    model = Article
    fields = ("title", "content", "status", "twitter_post")
    success_url = reverse_lazy("home")

class ArticleUpdateView(UpdateView):
    template_name = "articles/update_article.html"
    model = Article
    fields = ("title", "content", "status", "twitter_post")
    success_url = reverse_lazy("home")
    context_object_name = "article"

class ArticleDeleteView(DeleteView):
    template_name = "articles/delete_article.html"
    model = Article
    success_url = reverse_lazy("home")
    context_object_name = "article"