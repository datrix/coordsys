# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-31 07:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_student_degree'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='startYear',
            field=models.IntegerField(default=2014),
            preserve_default=False,
        ),
    ]