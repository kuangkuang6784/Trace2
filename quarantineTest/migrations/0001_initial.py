# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-03-20 11:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConsumerRegistry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ConsumerId', models.CharField(max_length=15)),
                ('ConsumerName', models.CharField(max_length=10)),
                ('ContactNo', models.IntegerField()),
                ('RegisterTimeConsumer', models.DateField(default=datetime.date(2019, 3, 20))),
                ('SearchCounts', models.IntegerField(default=0)),
                ('VIP', models.BooleanField(default=False)),
                ('Password', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='QuarantineData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QuarantineID', models.CharField(blank=True, max_length=10, null=True)),
                ('ProductionId', models.CharField(max_length=10)),
                ('QuarantineName', models.CharField(max_length=16)),
                ('QuarantinePersonID', models.CharField(max_length=10)),
                ('QuarantineLocation', models.CharField(max_length=100)),
                ('QuarantineRes', models.CharField(max_length=100)),
                ('QuarantineLink', models.CharField(blank=True, max_length=100, null=True)),
                ('QuarantineTime', models.DateField(default=datetime.date.today)),
                ('QuarantineBatch', models.CharField(max_length=50)),
                ('QuarantineUCLLink', models.CharField(blank=True, max_length=100, null=True)),
                ('Applicant', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='QuarantineRegistry',
            fields=[
                ('consumerregistry_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='quarantineTest.ConsumerRegistry')),
                ('QuarantinePersonID', models.CharField(max_length=10)),
                ('QuarantinerName', models.CharField(max_length=16)),
                ('IDNo', models.CharField(max_length=18)),
                ('ContactNo_Quar', models.BigIntegerField(blank=True, null=True)),
                ('RegisterTime', models.CharField(max_length=30)),
                ('WorkPlaceID', models.CharField(max_length=30)),
                ('PhotoSrc', models.CharField(blank=True, max_length=100, null=True)),
                ('CertificateNo', models.CharField(blank=True, max_length=32, null=True)),
                ('CertificateSrc', models.CharField(blank=True, max_length=100, null=True)),
                ('LicensedVeterinaryQCNo', models.CharField(blank=True, max_length=32, null=True)),
                ('LicensedVeterinaryQCSrc', models.CharField(blank=True, max_length=32, null=True)),
                ('QuarantineCounts', models.IntegerField(default=0)),
            ],
            bases=('quarantineTest.consumerregistry',),
        ),
    ]
