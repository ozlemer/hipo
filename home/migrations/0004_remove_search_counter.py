# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-27 22:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_search_search_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='search',
            name='counter',
        ),
    ]