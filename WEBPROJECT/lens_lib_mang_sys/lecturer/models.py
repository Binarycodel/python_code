from distutils.command.upload import upload
from django.db import models
from django import forms
# Create your models here.



class Lecturer(models.Model):

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    time_stamp = models.DateTimeField(auto_now_add=True)
    validate = models.BooleanField(default=False)
    # material = models.FileField(upload_to='material')


    def __str__(self) -> str:
        return f'Name : {self.name}    Email : {self.email}'


