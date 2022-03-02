from django.db import models

# Create your models here.
class Feature(models.Model):
    id: int
    name: str
    details: str
    is_true: bool
    # id = models.IntegerField()
    # name = models.CharField(max_length=20)
    # details = models.CharField(max_length=20)
    # is_true = models.BooleanField()
