# Generated by Django 2.1.4 on 2020-05-22 13:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('staff_user', '0007_auto_20200523_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hours',
            name='hours_today',
            field=models.CharField(default=0, max_length=16),
        ),
    ]
