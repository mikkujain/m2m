# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-02 11:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='data',
            new_name='file',
        ),
        migrations.RenameField(
            model_name='files',
            old_name='file_name',
            new_name='site',
        ),
        migrations.RenameField(
            model_name='site',
            old_name='site_name',
            new_name='directory',
        ),
    ]