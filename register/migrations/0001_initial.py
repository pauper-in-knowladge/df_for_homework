# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-24 19:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('pwd', models.CharField(max_length=50)),
                ('head_pic', models.CharField(default=0, max_length=255)),
                ('attr', models.IntegerField(default=0)),
            ],
        ),
    ]
