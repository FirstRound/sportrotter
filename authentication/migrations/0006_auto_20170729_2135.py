# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-29 21:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_galleryitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professional',
            name='background',
            field=models.FileField(blank=True, upload_to='backgrounds'),
        ),
        migrations.AlterField(
            model_name='professional',
            name='diploma',
            field=models.FileField(blank=True, upload_to='diplomas'),
        ),
        migrations.AlterField(
            model_name='professional',
            name='grade',
            field=models.CharField(choices=[('BEGINNER', 'Beginner'), ('AMATEUR', 'Amateur'), ('PROFESSIONAL', 'Professional')], default='AMATEUR', max_length=20),
        ),
    ]
