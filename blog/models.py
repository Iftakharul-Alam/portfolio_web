from django.db import models

# Create your models here.


class Blog(models.Model):
    heading = models.CharField(max_length=255)
    image = models.ImageField(upload_to='portfolio')
    video = models.URLField(null=True, blank=True)
    skills = models.CharField(max_length=255)
