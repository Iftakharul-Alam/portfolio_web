from django.db import models

# Create your models here.


class Resume(models.Model):
    title = models.CharField(max_length=100)
    field = models.CharField(max_length=100)
    expertize_details = models.TextField()
    learning_details = models.TextField()
    experience = models.IntegerField()


class Training(models.Model):
    title = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    learning_details = models.TextField()
    application_details = models.TextField()


class Skill(models.Model):
    topic = models.CharField(max_length=100)


class SkillDetail(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    sub_topic = models.CharField(max_length=100)
    value = models.IntegerField()

