# Generated by Django 4.0.4 on 2022-08-29 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElectronicBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('format', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('efile', models.FileField(upload_to='')),
            ],
        ),
    ]
