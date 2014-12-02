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
        migrations.AlterField(
            model_name='brigade',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(allow_duplicates=b'"\'False\'"', separator=b'\'"u\\\'-\\\'"\'', blank=True, populate_from=b'\'"\\\'title\\\'"\'', editable=False, verbose_name='slug', overwrite=b'"\'False\'"'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='initiative',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(allow_duplicates=b'"\'False\'"', separator=b'\'"u\\\'-\\\'"\'', blank=True, populate_from=b'\'"\\\'title\\\'"\'', editable=False, verbose_name='slug', overwrite=b'"\'False\'"'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='partner',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(allow_duplicates=b'"\'False\'"', separator=b'\'"u\\\'-\\\'"\'', blank=True, populate_from=b'\'"\\\'title\\\'"\'', editable=False, verbose_name='slug', overwrite=b'"\'False\'"'),
            preserve_default=True,
        ),
    ]
