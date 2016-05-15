# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-15 03:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OpenID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=254, unique=True)),
                ('time', models.TimeField()),
            ],
            options={
                'verbose_name': '\u7528\u6237\u7684\u90ae\u7bb1',
                'verbose_name_plural': '\u7528\u6237\u7684\u90ae\u7bb1',
            },
        ),
    ]