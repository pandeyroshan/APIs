from django.db import models

# Create your models here.

class dataSet(models.Model):
    topic = models.CharField(max_length=50,blank=False)
    text = models.TextField(blank=False)