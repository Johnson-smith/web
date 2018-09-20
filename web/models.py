from django.db import models
from django.contrib.auth.models import User


class UserProfile(User):
    cname = models.CharField("中文名称", max_length=30)