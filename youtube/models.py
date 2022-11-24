from django.db import models

# Create your models here.


class Video(models.Model):
    video_id = models.CharField(max_length=15, unique=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    channel = models.CharField(max_length=30)
    published_at = models.DateTimeField()
    thumbnail_url = models.URLField()
