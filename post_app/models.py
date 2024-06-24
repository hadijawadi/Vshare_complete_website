from django.db import models

from django.contrib.auth.models import User


class Create_text_post(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.user
