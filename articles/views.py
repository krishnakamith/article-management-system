from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Article
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class ArticleListView(LoginRequiredMixin, ListView):
    template_name = "articles/home.html"
    model = Article
    context_object_name = "articles"

    def get_queryset(self):
        return Article.objects.filter(creator=self.request.user).order_by("-created_at")

class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = "articles/article_create.html"
    model = Article
    fields = ("title", "content", "status", "twitter_post")
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "articles/article_update.html"
    model = Article
    fields = ("title", "content", "status", "twitter_post")
    success_url = reverse_lazy("home")
    context_object_name = "article"

    def test_func(self):
        return self.request.user == self.get_object().creator

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "articles/article_delete.html"
    model = Article
    success_url = reverse_lazy("home")
    
    context_object_name = "article"


    def test_func(self):
        return self.request.user == self.get_object().creator
    
    def post(self, request, *args, **kwargs):
        messages.success(request, "Article deleted successfully.", extra_tags="destructive")
        return super().delete(request, *args, **kwargs)