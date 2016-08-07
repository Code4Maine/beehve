# -*- coding: utf-8 -*-


from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='position',
            options={'ordering': ('order',)},
        ),
        migrations.AddField(
            model_name='position',
            name='order',
            field=models.IntegerField(default=0, verbose_name='Order'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='position',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(allow_duplicates=False, separator=b'\'"u\\\'-\\\'"\'', blank=True, populate_from=b'\'"\\\'title\\\'"\'', editable=False, verbose_name='slug', overwrite=False),
            preserve_default=True,
        ),
    ]
