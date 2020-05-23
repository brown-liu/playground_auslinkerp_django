# Generated by Django 2.1.4 on 2020-05-16 10:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('warehouse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='containers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctnr_number', models.CharField(max_length=64)),
                ('ctnr_type', models.CharField(max_length=32)),
                ('ctnr_eta', models.DateTimeField()),
                ('ctnr_owner', models.CharField(max_length=128)),
                ('ctnr_job', models.CharField(max_length=64)),
                ('ctnr_special', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='location_used',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('l_details', models.CharField(max_length=256)),
                ('l_time', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='carton_cloud_client',
            name='c_id',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]
