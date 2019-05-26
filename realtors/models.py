from django.db import models

# Create your models here.

from datetime import datetime

# Create your models here.
class Realtor(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_mvp= models.BooleanField(default=True)
    hire_date_date= models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name
