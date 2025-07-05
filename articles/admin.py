from django.contrib import admin
from articles.models import UserProfile, Article

admin.site.register(Article)
admin.site.register(UserProfile)