# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 12:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0002_auto_20171202_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notebook',
            name='name',
            field=models.CharField(max_length=500, unique=True),
        ),
    ]
