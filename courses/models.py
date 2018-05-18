from django.db import models
from datetime import datetime

# Create your models here.

class Sublistcontent(models.Model):
    sublistcontent_text = models.TextField(max_length=1000, null=True)

    def __str__(self):
        return self.sublistcontent_text

class Listcontent(models.Model):
    title_id = models.CharField(max_length=200, default=None)
    listcontent_text = models.TextField(max_length=5000, null=True)
    sublistcontent = models.ForeignKey(Sublistcontent, on_delete=models.CASCADE, default=None)
    
    def __str__(self):
        return self.title_id

class Course(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=500, null=True)
    objtext = models.TextField(max_length=5000, null=True)
    objectives = models.TextField(max_length=5000, null=True)
    listheader = models.CharField(max_length=100, null=True)
    listcontent = models.ForeignKey(Listcontent, on_delete=models.CASCADE, default=None)
    target = models.CharField(max_length=500, null=True)
    cost = models.CharField(max_length=500, null=True) 
    # dates = models.DateTimeField(null=True)
    
    def __str__(self):
        return self.title