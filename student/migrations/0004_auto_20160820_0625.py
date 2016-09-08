# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-20 06:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20160820_0525'),
        ('student', '0003_enrol'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrol',
            name='course_new',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course_new', to='course.course'),
        ),
        migrations.AddField(
            model_name='enrol',
            name='zID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.student'),
        ),
        migrations.AlterField(
            model_name='enrol',
            name='course_old',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course_old', to='course.course'),
        ),
    ]
