# Generated by Django 4.0.4 on 2022-09-06 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecturer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecturer',
            name='validate',
            field=models.BooleanField(default=False),
        ),
    ]
