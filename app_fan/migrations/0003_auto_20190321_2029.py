# Generated by Django 2.1.7 on 2019-03-21 12:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190321_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyregistry',
            name='RegisterTime',
            field=models.DateField(verbose_name=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='producerregistry',
            name='RegisterTime',
            field=models.DateField(verbose_name=datetime.date.today),
        ),
    ]
