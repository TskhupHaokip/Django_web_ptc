from django.contrib.auth.base_user import BaseUserManager
from django.db import models

from datetime import timedelta, timezone
from django.utils import timezone


class SubscriptionManager(models.Manager):
    def create_subscription(self, user, plan="pro", expires_at=None):
        if expires_at is None:
            expires_at = timezone.now() + timedelta(minutes=30)

        return self.create(
            user=user,
            plan=plan,
            expires_at=expires_at,
        )


class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        try:
            if not username:
                raise ValueError("Username is required")
            user = self.model(
                username=username,
                **extra_fields
            )

            user.set_password(password)
            user.save(using=self._db)

            return user
        except Exception as e:
            return f"Error {str(e)}"

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self.create_user(
            username=username,
            password=password,
            **extra_fields
        )