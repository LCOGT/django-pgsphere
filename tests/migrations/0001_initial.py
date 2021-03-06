# -*- coding: utf-8 -*-
# Generated by Django 1.9b1 on 2015-11-17 17:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import pgsphere.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', pgsphere.fields.SBoxField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', pgsphere.fields.SPointField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
