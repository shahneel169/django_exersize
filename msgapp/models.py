from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    message = models.CharField(max_length=255)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
