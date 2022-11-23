from django.db import models

class User(models.Model):
  name = models.CharField(max_length=100)
  email = models.TextField(max_length=100)
  phone = models.CharField(max_length=100, default='')
  gender = models.CharField(max_length=100, default='')
  dob = models.TextField(max_length=100, default='')

class Doctor(models.Model):
  drID = models.CharField(max_length=20, default='')
  name = models.CharField(max_length=100)
  languages = models.TextField()
  gender = models.CharField(max_length=1)
  qualifications = models.TextField()
  specialty = models.CharField(max_length=10, default='')