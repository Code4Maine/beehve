# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20141202_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='brigade',
            name='chat',
            field=models.CharField(max_length=255, null=True, verbose_name='Chat link', blank=True),
            preserve_default=True,
        ),
    ]
