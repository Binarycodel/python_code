# Generated by Django 4.0.4 on 2022-09-07 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lecturer', '0003_lecturer_material'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecturer',
            name='material',
        ),
    ]