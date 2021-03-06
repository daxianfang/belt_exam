# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-16 15:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('belt_app', '0002_auto_20161216_1545'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friendsfriend', to='belt_app.User')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usersfriend', to='belt_app.User')),
            ],
        ),
    ]
