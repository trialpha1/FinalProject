# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-07 05:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codex', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='class',
            old_name='ClassName',
            new_name='Class',
        ),
    ]
