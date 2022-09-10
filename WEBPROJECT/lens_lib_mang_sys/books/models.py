from pyexpat import model
from secrets import choice
from django.db import models
from django import forms

# Create your models here.


class Materials(models.Model):

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

    past_q = 'PastQ'
    hand_out = 'handout'

    MATERIAL = [
        (past_q, 'Past Question'), 
        (hand_out, "Handout")
    ]
    
    lecturer = models.CharField(max_length=100)
    course_code = models.CharField(max_length=100) 
    course_title = models.CharField(max_length=100)
    year = models.IntegerField()

    material_type = models.CharField(
        max_length = 50, 
        choices = MATERIAL, 
        default = hand_out
    )

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
    
    efile = models.FileField(upload_to='material')

    def __str__(self) -> str:
        return f' CODE: {self.course_code}   COURSE TITLE:  {self.course_title}'


