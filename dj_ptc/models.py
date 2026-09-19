from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from datetime import timedelta, timezone
from django.utils import timezone
from .managers import UserManager,SubscriptionManager

class Subscription(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    plan = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    objects = SubscriptionManager()
    
    def upgrade_plan(self,plan:str):
        plans = ["free","pro","bussiness"]
        if plan not in plans:
            return f"No Plan {plan}"
        if plan == "pro":
            self.plan = "pro"
            expires_at = timezone.now() + timedelta(minutes=120)
        elif plan == "bussiness":
            self.plan = "bussiness"
            expires_at = timezone.now() + timedelta(minutes=250)
        self.save()
        return f"Plan {plan} Upgraded Sucessfully"

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.username