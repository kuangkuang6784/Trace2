# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-03-20 11:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quarantineTest', '0002_auto_20190320_1913'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quarantinedata',
            old_name='QuarantineName',
            new_name='QuarantinerName',
        ),
    ]
