
from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


    # matric_number = models.CharField(max_length=100)
    # student_name = models.CharField(max_length=100)
    # password = models.CharField(max_length=100)
    # time_stamp = models.DateTimeField(auto_now_add=True)
    # email = models.EmailField()
    # validate = models.BooleanField(default=False)

class StudentUser(AbstractUser):
    pass
    matric_number = models.CharField(max_length=100)
    # student_name = models.CharField(max_length=100)
    # password = models.CharField(max_length=100)
    # time_stamp = models.DateTimeField(auto_now_add=True)
    # email = models.EmailField()

    

