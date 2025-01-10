from django.db import models

# Create your models here.
class Flowers(models.Model):
    flower_name = models.CharField(max_length=30)
    flower_id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

class User(models.Model):
    name = models.CharField(max_length=30)
    id = models.IntegerField(primary_key=True)
    account = models.CharField(max_length=40)
    email = models.CharField(max_length=50)