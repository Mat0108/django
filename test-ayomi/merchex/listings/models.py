from django.db import models

class User(models.Model):
    mail = models.fields.CharField(max_length=100)
    password = models.fields.CharField(max_length=100)
