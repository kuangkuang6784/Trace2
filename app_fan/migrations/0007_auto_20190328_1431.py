# Generated by Django 2.1.7 on 2019-03-28 06:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20190327_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producerregistry',
            name='CompanyName',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='producerregistry',
            name='IDNo',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='producerregistry',
            name='InvestigateRes',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='producerregistry',
            name='ProductionKind',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='producerregistry',
            name='ProductionPlace',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='producerregistry',
            name='ProductionScale',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='producerregistry',
            name='RegisterTime',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='producerregistry',
            name='SecretKeys',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
