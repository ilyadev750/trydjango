from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.TextField(blank=True, null=True)
    age = models.PositiveIntegerField()
    city = models.TextField(default='Moscow')