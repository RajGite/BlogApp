# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-05 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=128)),
                ('category', models.CharField(max_length=128)),
            ],
        ),
    ]