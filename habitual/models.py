from django.db import models


class Habit(models.Model):
    name = models.CharField(max_length=80)
    amount = models.IntegerField()
