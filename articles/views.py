from django.shortcuts import render, redirect
from .models import Article
from .forms import CreateArticleForms

def home(request):
    articles = Article.objects.all()
    return render(request, "articles/home.html", {"articles" : articles})

def create_article(request):
    if request.method == "POST":
        form = CreateArticleForms(request.POST)
        if form.is_valid:
            form_data = form.cleaned_data
            new_article = Article(
                title = form_data["title"],
                content = form_data["content"],
                status = form_data["status"],
                word_count = form_data["word_count"],
                twitter_post = form_data["twitter_post"],
            )
            new_article.save()
            return redirect("home")
    else:
        form = CreateArticleForms()
        return render(request, "articles/create_article.html", {"form" : form})