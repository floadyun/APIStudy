from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=10)
    phone = models.CharField(max_length=13)
    sex = models.CharField(max_length=5)
    age = models.IntegerField(default=0)