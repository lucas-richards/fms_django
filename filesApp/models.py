from django.db import models


class File(models.Model):
    title = models.CharField(max_length=255)
    version = models.CharField(max_length=20, default='A1')
    document = models.FileField(upload_to="docs")
    last_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)