# Generated by Django 2.1.4 on 2020-05-20 20:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('warehouse', '0002_auto_20200516_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='containers',
            name='ctnr_eta',
            field=models.DateField(),
        ),
    ]