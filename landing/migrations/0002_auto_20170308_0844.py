# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-08 08:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subscribes',
            new_name='Subscriber',
        ),
    ]
