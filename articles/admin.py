from django.contrib import admin
from articles.models import UserProfile, Article
from django.contrib.auth.admin import UserAdmin

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "word_count", "status", "created_at", "updated_at")
    list_filter = ("status",)
    search_fields = ("title", "content")
    date_hierarchy = "created_at"
    ordering = ("created_at",)
    readonly_fields = ("word_count", "created_at", "updated_at")

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        ("Credentials", {"fields": ("email", "password")}),
        ("Personal information", {"fields": ("first_name", "last_name")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        ("Credentials", {
            "classes": ("wide", "collapse"),
            "fields": ("email", "password1", "password2"),
        }),
    )
    list_display = ("email", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(Article, ArticleAdmin)
admin.site.register(UserProfile, CustomUserAdmin)