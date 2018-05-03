from django.db import models
from datetime import datetime

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=500)
    objtext = models.TextField(max_length=5000)
    objectives = models.TextField(max_length=5000)
    listheader = models.CharField(max_length=100)
    listcontent = models.TextField(max_length=5000)
    #sublistcontent = models.TextField(blank=True, null=True)
    target = models.CharField(max_length=500)
    cost = models.CharField(max_length=500) 
    dates = models.DateTimeField()
    
    def __str__(self):
        return self.title