# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-17 11:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20160417_1717'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='username',
            new_name='user_name',
        ),
    ]
