# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-08 04:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codex', '0004_auto_20171207_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='picture',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='race',
            name='picture',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='spell',
            name='picture',
            field=models.CharField(default='', max_length=250),
        ),
    ]
