# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-20 06:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20160820_0525'),
        ('student', '0002_auto_20160820_0457'),
    ]

    operations = [
        migrations.CreateModel(
            name='enrol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_old', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_old', to='course.course')),
            ],
        ),
    ]