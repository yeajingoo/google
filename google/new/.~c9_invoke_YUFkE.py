from django.db import models


class student(models.Model):
    name = models.CharField(max_length=200)
    g
    age = models.IntegerField()
    description = models.TextField()
    
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
      return self.title
    