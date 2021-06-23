from django.db import models
from datetime import datetime

class Listing(models.Model):
    name = models.CharField(max_Length = 200)
    photo = models.ImageField(upload_to = 'photos/%y/%m/%d/')
    description = models.TextField(blank = True)
    phone = models.CharField(max_Length = 20)
    email = models.CharField(max_Length = 20)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(defaulat = datetime.now, blank=True)
    def __str__(self):
        return self.name
