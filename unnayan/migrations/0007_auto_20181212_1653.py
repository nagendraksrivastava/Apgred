# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-12 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unnayan', '0006_auto_20181203_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyprofile',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='companyprofile',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
