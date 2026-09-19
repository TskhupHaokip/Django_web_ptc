from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Subscription

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "plan", "created_at", "expires_at")
    list_display_links = (
        "id",
        "user",
        "plan",
    )

   

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("id", "username", "is_active", "is_staff")
    list_display_links = ("username",)

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "groups", "user_permissions")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "password1", "password2"),
        }),
    )