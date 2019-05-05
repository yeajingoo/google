from django.db import models
from django import forms

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    writer = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    userId=model.CharField(max_length=200)
  
    
    def __str__(self):
      return self.title