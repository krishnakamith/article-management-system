import re

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from .managers import UserProfileManager

ARTICLE_STATUS = (
            ("draft", "draft"),
            ("inprogress", "in progress"),
            ("published", "published"),
        )

class UserProfile(AbstractUser):
    email = models.EmailField("email address", max_length=255, unique=True)
    objects = UserProfileManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    @property
    def article_count(self):
        return self.articles.count()
    
    @property
    def written_words(self):
        return self.articles.aggregate(models.Sum("word_count"))["word_count__sum"] or 0


class Article(models.Model):
    title = models.CharField("Heading", max_length=100)
    content = models.TextField(blank=True, default="")
    word_count = models.IntegerField()
    twitter_post = models.TextField(blank=True, default="")
    status = models.CharField(
        max_length=20, 
        choices = ARTICLE_STATUS,
        default = "draft",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="articles")

    def save(self, *args, **kwargs):
        text = re.sub(r"<[^>]*>", "", self.content).replace("&nbsp;", " ")
        self.word_count = len(re.findall(r"\b\w+\b", text))
        super().save(*args, **kwargs)