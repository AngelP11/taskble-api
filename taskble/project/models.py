from django.db import models
from datetime import datetime
# Create your models here.

class File(models.Model):
    name = models.CharField("Name",max_length=150)

class Card (models.Model):
    name = models.CharField("Name Card", max_length=100)

class Category (models.Model):
    name = models.CharField("Name Category", max_length=100)

class SubTask (models.Model):
    title = models.CharField("Title", max_length=100)
    description = models.CharField("Description", max_length=100)

class Task (models.Model):
    title = models.CharField("Title", max_length=100)
    description = models.CharField("Description", max_length=255)
    ruls = [('rule1','Rule'),('rule2','Rule 2')]
    rules = models.CharField(max_length=6, choices=ruls, default='rule1')
    predetermined = models.BooleanField("predetermined")
    file = models.ManyToManyField(File)
    subtask = models.ManyToManyField(SubTask)
    card = models.ManyToManyField(Card)

class Project (models.Model):
    name = models.CharField("Name", max_length=100)
    time = models.DateField("Time", default=datetime.now)
    state = [('active','Active'),('closed','Closed')]
    status = models.CharField(max_length=6, choices=state, default='active')
    comment = models.TextField("Comment")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)