# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-20 21:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('videos', '0003_relation_comment_relation_comment_proj'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='favorite',
            unique_together=set([('user', 'video')]),
        ),
    ]