# Generated by Django 4.0.4 on 2022-09-02 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_materials_efile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materials',
            name='efile',
            field=models.FileField(upload_to='material'),
        ),
    ]
