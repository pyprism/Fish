# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 14:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0004_auto_20171203_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='note_book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='note.NoteBook'),
        ),
    ]