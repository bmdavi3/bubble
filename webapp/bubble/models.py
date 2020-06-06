from django.db import models


class Jug(models.Model):
    name = models.TextField()

    class Meta:
        db_table = 'jug'


class Bubble(models.Model):
    jug = models.ForeignKey(Jug, on_delete=models.CASCADE)
    created = models.DateTimeField()  # A DB level default of now() is added in a manual migration

    class Meta:
        db_table = 'bubble'

