from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length = 64)
    inventory = ArrayField(models.IntegerField(), default = list)
