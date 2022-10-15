from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)


class Portfolio(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    heading = models.CharField(max_length=255)
    image = models.ImageField(upload_to='portfolio')
    link = models.URLField()

