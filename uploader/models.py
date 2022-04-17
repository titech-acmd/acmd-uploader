from django.db import models


# Create your models here.

class File(models.Model):
    Filename = models.CharField(max_length=1000)
    FileOwner = models.CharField(max_length=50)
    UploadDate = models.DateTimeField('date uploaded')
    file = models.FileField(
        upload_to='uploads/%Y/%m/%d',
    )
    PersonalToken = models.CharField(max_length=200)