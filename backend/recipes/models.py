from django.db import models

class Recipe(models.Model):
    name = models.TextField(max_length = 20)
    email = models.EmailField(unique = True)
    content = models.TextField(max_length = 600)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager