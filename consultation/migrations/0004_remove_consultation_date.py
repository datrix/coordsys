# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-23 13:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0003_auto_20160823_1322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consultation',
            name='date',
        ),
    ]