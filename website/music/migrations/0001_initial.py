# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-14 12:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=250)),
                ('album_title', models.CharField(max_length=500)),
                ('gener', models.CharField(max_length=500)),
                ('album_logo', models.CharField(max_length=1000)),
            ],
        ),
    ]
