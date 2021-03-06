# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-28 17:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0002_auto_20160428_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='address',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='project',
            name='project',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userprofiles.ProjectType'),
        ),
    ]
