# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-04 21:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0010_remove_category_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Implique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grand', to='videos.Tag')),
                ('petit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='petit', to='videos.Tag')),
            ],
        ),
    ]
