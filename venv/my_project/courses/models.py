from django.db import models

# Create your models here.
class Course(models.Model):
    c_name = models.CharField(max_length=100)
    c_id = models.CharField(max_length=100)
    c_duration = models.PositiveBigIntegerField()
    c_faculty = models.CharField(max_length=100)