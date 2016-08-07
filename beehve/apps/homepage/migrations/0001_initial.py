# -*- coding: utf-8 -*-


from django.db import models, migrations
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('honey', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brigade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', django_extensions.db.fields.AutoSlugField(allow_duplicates=False, separator=b'"u\'-\'"', blank=True, populate_from=b'"\'title\'"', editable=False, verbose_name='slug', overwrite=False)),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
                ('phone', models.CharField(max_length=20, null=True, verbose_name='Phone', blank=True)),
                ('meetup', models.CharField(max_length=255, null=True, verbose_name='Meetup link', blank=True)),
                ('chat', models.CharField(max_length=255, null=True, verbose_name='Chat link', blank=True)),
                ('github', models.CharField(max_length=255, null=True, verbose_name='Github link', blank=True)),
                ('twitter', models.CharField(max_length=100, null=True, verbose_name='Twitter username', blank=True)),
                ('facebook', models.CharField(max_length=100, null=True, verbose_name='Facebook username', blank=True)),
                ('instagram', models.CharField(max_length=100, null=True, verbose_name='Instagram username', blank=True)),
                ('background', models.CharField(max_length=255, null=True, verbose_name='Dashboard background color or URL', blank=True)),
                ('active', models.BooleanField(default=True, verbose_name='Is brigade active?')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Initiative',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', django_extensions.db.fields.AutoSlugField(allow_duplicates=False, separator=b'"u\'-\'"', blank=True, populate_from=b'"\'title\'"', editable=False, verbose_name='slug', overwrite=False)),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
                ('area', models.CharField(help_text=b'Examples: State-wide, Pilsen Neighborhood, etc.', max_length=255, null=True, verbose_name='Area', blank=True)),
                ('year', models.CharField(max_length=4, null=True, verbose_name='Year', blank=True)),
                ('logo', models.ImageField(upload_to=b'homepage/initiatives', null=True, verbose_name='Logo', blank=True)),
                ('active', models.BooleanField(default=True, verbose_name='Is initiative active?')),
                ('brigade', models.ForeignKey(to='homepage.Brigade')),
                ('projects', models.ManyToManyField(to='honey.Project', null=True, blank=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', django_extensions.db.fields.AutoSlugField(allow_duplicates=False, separator=b'"u\'-\'"', blank=True, populate_from=b'"\'title\'"', editable=False, verbose_name='slug', overwrite=False)),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
                ('partner_type', models.CharField(max_length=255, null=True, verbose_name='Type', blank=True)),
                ('year', models.CharField(max_length=4, null=True, verbose_name='Year', blank=True)),
                ('logo', models.ImageField(upload_to=b'homepage/partners', null=True, verbose_name='Logo', blank=True)),
                ('active', models.BooleanField(default=True, verbose_name='Is partnership active?')),
                ('brigade', models.ForeignKey(to='homepage.Brigade')),
                ('projects', models.ManyToManyField(to='honey.Project', null=True, blank=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
            bases=(models.Model,),
        ),
    ]
