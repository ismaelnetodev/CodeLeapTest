from django.db import models
from django.utils.timezone import now
# Create your models here.
class Post(models.Model):
    username = models.CharField(max_length=255)
    created_datetime = models.DateTimeField(default=now)
    title = models.CharField(max_length=255)
    content = models.TextField()
    
    def __str__(self):
        return self.title
