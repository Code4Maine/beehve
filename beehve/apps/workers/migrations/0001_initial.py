# -*- coding: utf-8 -*-


from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', django_extensions.db.fields.AutoSlugField(allow_duplicates=False, separator=b'"u\'-\'"', blank=True, populate_from=b'"\'title\'"', editable=False, verbose_name='slug', overwrite=False)),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
                ('brigade', models.ForeignKey(to='homepage.Brigade')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Name', blank=True)),
                ('why', models.TextField(null=True, verbose_name='Why I am part of Code 4 Maine', blank=True)),
                ('website', models.CharField(max_length=200, null=True, verbose_name='Personal website', blank=True)),
                ('phone', models.CharField(max_length=20, null=True, verbose_name='Phone', blank=True)),
                ('city', models.CharField(max_length=100, null=True, verbose_name='City', blank=True)),
                ('skype', models.CharField(max_length=100, null=True, verbose_name='Skype username', blank=True)),
                ('github', models.CharField(max_length=100, null=True, verbose_name='Github username', blank=True)),
                ('twitter', models.CharField(max_length=100, null=True, verbose_name='Twitter username', blank=True)),
                ('facebook', models.CharField(max_length=100, null=True, verbose_name='Facebook username', blank=True)),
                ('instagram', models.CharField(max_length=100, null=True, verbose_name='Instagram username', blank=True)),
                ('linkedin', models.CharField(max_length=100, null=True, verbose_name='LinkedIn username', blank=True)),
                ('email_notify', models.BooleanField(default=True, verbose_name='Email notifications on updates')),
                ('active', models.BooleanField(default=True, verbose_name='Is worker active?')),
                ('position', models.ForeignKey(blank=True, to='workers.Position', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
            bases=(models.Model,),
        ),
    ]
