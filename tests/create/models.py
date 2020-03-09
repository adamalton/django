from django.db import models


class Musician(models.Model):
    name = models.CharField(max_length=100, unique=True)
    num_bands = models.PositiveIntegerField()


class Song(models.Model):
    musician = models.ForeignKey(Musician, primary_key=True, on_delete=models.CASCADE)
