from distutils.command.upload import upload
from lzma import MODE_NORMAL
from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class StudentUser(models.Model):

#===================================  department in lens
    com = 'COM'
    ecc = 'ECC'
    cet = 'CET'
    sta = 'STA'
    tel = 'TEL'
    slt = 'SLT'
    mac = 'MAC'
    mmt = 'MMT'
    agd = 'AGD'
    bam = 'BAM'
    acc = 'ACC'
    mcb = 'MCB'
    bch = 'BCH'

    DEPT = [
        (com, 'Com Science'),
        (ecc, 'Electrical'),
        (cet, 'Com engine'),
        (sta, 'Statistic'),
        (slt, 'Scn Lab Tech'),
        (mac, 'Mass Com'),
        (mmt, 'Mult Media'),
        (agd, 'Graphics'),
        (bam, 'Buss Admin'),
        (acc, 'Accounting'),
        (mcb, 'Micro Bio'),
        (bch, 'Biochem')
    ]
#  ==============================end of department 
    nd1 = 'ND1'
    nd2 = 'ND2'
    hnd1 = 'HND1'
    hnd2 = 'HND2'

    LEVEL = [
        (nd1 , 'National Deploma 1'), 
        (nd2, 'National Deploma 2'), 
        (hnd1, 'Higher National Deploma 1'), 
        (hnd2, 'Higher National Deploma 2')
    ]
# ======================== LEVEL OPTIONS ==========================

    matric_number = models.CharField(max_length=100)
    student_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    time_stamp = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    # e_type = models.CharField(max_length=100)
    level = models.CharField(
        max_length=50, 
        choices=LEVEL,
        default=nd1
    )

    department = models.CharField(
        max_length=7,
        choices=DEPT,
        default=com,
    )
    # dept = models.CharField(max_length=50) 
    validate = models.BooleanField(default=False)
    passport = models.ImageField(upload_to='passport')

def __str__(self) -> str:
    return f'Matric Num : {self.matric_number}   Student Name : {self.student_name}'



class ElectronicBook(models.Model):
    isbn = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    format = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    efile = models.FileField(upload_to='media')


    def __str__(self) -> str:
        return f' TITLE: {self.title}   ISBN:  {self.isbn}'