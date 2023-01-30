from django.db import models

class Transactions(models.Model):
    type = models.IntegerField()
    date_and_hour = models.DateTimeField()
    value = models.FloatField()
    cpf = models.IntegerField()
    card = models.CharField(max_length=12)
    owner = models.CharField(max_length=14)
    name = models.CharField(max_length=19)
