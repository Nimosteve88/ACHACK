from django.db import models

# Create your models here.
class Person(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    btac_score = models.IntegerField()
    eas_score = models.IntegerField()
    fl_score = models.IntegerField()
    hr_score = models.IntegerField()
    kf_score = models.IntegerField()
    mhawb_score = models.IntegerField()