from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    age = models.TextField()
    city = models.TextField(default='Moscow')