from django.db import models


class World(models.Model):
    name=models.CharField(max_length=150)
    description=models.TextField()
