from django.urls import path
from .views import (
    ArticleListView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
)

urlpatterns = [
    path("", ArticleListView.as_view(), name='home'),
    path("articles/create/", ArticleCreateView.as_view(), name="create_article"),
    path("articles/<int:pk>/update/", ArticleUpdateView.as_view(), name="update_article"),
    path("articles/<int:pk>/delete/", ArticleDeleteView.as_view(), name="delete_article")
]