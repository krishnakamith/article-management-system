from django.urls import path
from .views import home, CreateArticleView

urlpatterns = [
    path("", home, name='home'),
    path("articles/create/", CreateArticleView.as_view(), name="create_article"),
]