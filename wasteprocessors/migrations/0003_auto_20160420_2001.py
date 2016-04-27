# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-20 20:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wasteprocessors', '0002_auto_20160417_2057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user_type',
        ),
        migrations.RemoveField(
            model_name='project',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_type',
        ),
        migrations.RemoveField(
            model_name='waste',
            name='material',
        ),
        migrations.RemoveField(
            model_name='waste',
            name='project',
        ),
        migrations.RemoveField(
            model_name='waste',
            name='waste_type',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='ProjectType',
        ),
        migrations.DeleteModel(
            name='UserType',
        ),
        migrations.DeleteModel(
            name='Waste',
        ),
    ]