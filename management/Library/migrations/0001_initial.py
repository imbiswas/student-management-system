# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-06 10:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Book_Name', models.CharField(max_length=25)),
                ('ISBN_No', models.DecimalField(decimal_places=0, max_digits=13)),
                ('Purchase_date', models.DateField()),
                ('Book_No', models.CharField(max_length=5)),
                ('Auther', models.CharField(max_length=15)),
                ('Edition', models.CharField(max_length=10)),
                ('Publisher', models.CharField(max_length=20)),
                ('No_Of_Copies', models.DecimalField(decimal_places=0, max_digits=3)),
                ('Shelf_No', models.DecimalField(decimal_places=0, max_digits=5)),
                ('Book_Cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Language', models.CharField(max_length=15)),
                ('Condition', models.CharField(choices=[('As-New', 'As-New'), ('Fine', 'Fine'), ('Good', 'Good'), ('Fair', 'Fair'), ('Poor', 'Poor'), ('Missing', 'Missing'), ('Lost', 'Lost')], max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_Name', models.CharField(max_length=15)),
                ('Section_Code', models.DecimalField(decimal_places=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Issue_Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Issue_date', models.DateField()),
                ('Due_Date', models.DateField()),
                ('Book_No', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Library.Books')),
                ('Student_Unique_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student.Student_Admission')),
            ],
        ),
        migrations.CreateModel(
            name='Return_Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Return_or_Renewal', models.CharField(choices=[('Return', 'Return'), ('Renewal', 'Renewal')], max_length=7)),
                ('Date', models.DateField()),
                ('Fine_Amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Remarks', models.TextField()),
                ('Book_No', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Library.Books')),
            ],
        ),
        migrations.AddField(
            model_name='books',
            name='Category_Name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Library.Category'),
        ),
    ]
