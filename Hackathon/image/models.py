from django.db import models

# Create your models here.
class image(models.Model):
    file_op=models.FileField( upload_to='file')
