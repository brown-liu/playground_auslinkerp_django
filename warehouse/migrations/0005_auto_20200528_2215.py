# Generated by Django 2.1.4 on 2020-05-28 10:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('warehouse', '0004_auto_20200528_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='containers',
            name='ctnr_job',
            field=models.CharField(max_length=256),
        ),
    ]
