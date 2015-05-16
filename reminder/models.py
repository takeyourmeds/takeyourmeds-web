from django.db import models

class Reminder(models.Model):
    # freq = models.IntegerField()
    schedule = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
