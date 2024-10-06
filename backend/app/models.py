from django.db import models

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    photo_url = models.URLField()

class Resource(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField()
