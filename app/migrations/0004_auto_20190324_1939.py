# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-03-24 11:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_trance_produce_transportdata'),
    ]

    operations = [
        migrations.DeleteModel(
            name='trance_produce',
        ),
        migrations.DeleteModel(
            name='TransportData',
        ),
    ]
