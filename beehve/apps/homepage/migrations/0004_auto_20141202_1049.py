# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20141202_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='partner_type',
            field=models.CharField(max_length=255, null=True, verbose_name='Type', blank=True),
            preserve_default=True,
        ),
    ]
