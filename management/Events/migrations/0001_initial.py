# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-05 06:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Event_Name', models.CharField(max_length=25)),
                ('Description', models.TextField()),
                ('Startdate', models.DateField()),
                ('Enddate', models.DateField()),
                ('Organizer', models.CharField(max_length=20)),
                ('Remarks', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Event_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EventType', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='EventType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Events.Event_Type'),
        ),
    ]
