# Generated by Django 4.0.4 on 2022-08-31 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_studentuser_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentuser',
            name='dept',
        ),
        migrations.AddField(
            model_name='studentuser',
            name='department',
            field=models.CharField(choices=[('COM', 'Com Science'), ('ECC', 'Electrical'), ('CET', 'Com engine'), ('STA', 'Statistic'), ('SLT', 'Scn Lab Tech'), ('MAC', 'Mass Com'), ('MMT', 'Mult Media'), ('AGD', 'Graphics'), ('BAM', 'Buss Admin'), ('ACC', 'Accounting'), ('MCB', 'Micro Bio'), ('BCH', 'Biochem')], default='COM', max_length=7),
        ),
    ]
