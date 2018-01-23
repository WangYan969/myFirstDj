# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-23 03:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.CharField(db_column='user_id', max_length=100, primary_key=True, serialize=False)),
                ('userName', models.CharField(db_column='user_name', max_length=100)),
                ('passWord', models.CharField(db_column='user_pass', max_length=100)),
                ('photo', models.CharField(db_column='user_photo', max_length=100)),
            ],
        ),
    ]