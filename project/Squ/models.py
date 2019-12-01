from django.db import models

class Squirrel(models.Model):
    Latitude = models.IntegerField
    Longitude = models.IntegerField
    Id = models.CharField(max_length=200)
    Shift = models.CharField(max_length=200)
    Date = models.CharField(max_length=200)
    Age = models.CharField(max_length=200)
    Furcolor = models.CharField(max_length=200)
    Location = models.CharField(max_length=200)
    Speci_loc = models.CharField(max_length=200)
    Running =  models.BooleanField
    Chasing =  models.BooleanField
    Climbing =  models.BooleanField
    Eating =  models.BooleanField
    Foraging =  models.BooleanField
    Other_act = models.CharField(max_length=200)
    Kuks =  models.BooleanField
    Quaas =  models.BooleanField
    Moans =  models.BooleanField
    Tail_flag =  models.BooleanField
    Tail_twitch =  models.BooleanField
    Approaches =  models.BooleanField
    Indifferent =  models.BooleanField
    Runs_from =  models.BooleanField


# Create your models here.
