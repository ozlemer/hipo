# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-25 08:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Searches',
            new_name='Search',
        ),
        migrations.RenameField(
            model_name='search',
            old_name='search',
            new_name='tag',
        ),
    ]