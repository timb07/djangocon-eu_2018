# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-14 15:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0004_auto_20180514_1520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='square_meters',
        ),
    ]