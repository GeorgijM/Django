from django.db import models


class Idzin(models.Model):
    code_idzin = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=4000)

