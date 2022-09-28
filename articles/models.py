from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=120, )
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True) # when was created
    updated = models.DateTimeField(auto_now=True) # when updates
    publish = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True)
