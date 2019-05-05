from django.db import models



class Post(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=200)
    content = models.TextField()
    
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name=models.CharField(max_length=200,null=True)
    country=models.CharField(max_length=200,null=True)
    region=models.CharField(max_length=200,null=True)
    age=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    introduction=models.TextField(null=True)
    
    def __str__(self):
      return self.title
