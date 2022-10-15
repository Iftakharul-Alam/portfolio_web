from django.db import models


# Create your models here.

class About(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='profile')
    cover_photo = models.ImageField(upload_to='profile', null=True, blank=True)
    interests = models.TextField()
    hobbies = models.TextField()
    general_desc = models.TextField()
    headings = models.TextField(null=True, blank=True)
    youtube = models.URLField()
    facebook = models.URLField()
    linked_in = models.URLField()
    website = models.URLField()
    key_points = models.CharField(max_length=255, null=True, blank=True)


class PersonalInfo(models.Model):
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100)


class Language(models.Model):
    key = models.CharField(max_length=100)
    reading = models.IntegerField()
    writing = models.IntegerField()
    speaking = models.IntegerField()


class IELTS(models.Model):
    key = models.CharField(max_length=100)
    value = models.IntegerField()

    class Meta:
        verbose_name = 'IELTS'
        verbose_name_plural = 'IELTS'


class GRE(models.Model):
    key = models.CharField(max_length=100)
    value = models.IntegerField()

    class Meta:
        verbose_name = 'GRE'
        verbose_name_plural = 'GRE'


class PersonalSkill(models.Model):
    key = models.CharField(max_length=100)
    value = models.IntegerField()


class Education(models.Model):
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    institute = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    description = models.TextField()


class JOBS(models.Model):
    position = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    duties = models.CharField(max_length=100)
    achievement = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'JOBS'
        verbose_name_plural = 'JOBS'
