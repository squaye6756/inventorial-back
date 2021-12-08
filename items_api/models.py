from django.db import models
from stores_api.models import Store

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=64)
    price = models.IntegerField()
    quantity = models.IntegerField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True)
