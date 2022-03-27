from django.db import models
from django.contrib.auth.models import User

class Notes(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    guns = models.CharField(max_length = 100)
    knives = models.CharField(max_length = 100)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
