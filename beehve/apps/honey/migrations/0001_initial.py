# -*- coding: utf-8 -*-


from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Buzz',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', django_extensions.db.fields.AutoSlugField(allow_duplicates=False, separator=b'"u\'-\'"', blank=True, populate_from=b'"\'title\'"', editable=False, verbose_name='slug', overwrite=False)),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', django_extensions.db.fields.AutoSlugField(allow_duplicates=False, separator=b'"u\'-\'"', blank=True, populate_from=b'"\'title\'"', editable=False, verbose_name='slug', overwrite=False)),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
                ('pending', models.BooleanField(default=True)),
                ('project_count', models.IntegerField(default=0)),
                ('start_date', models.DateField(verbose_name='Start date')),
                ('start_time', models.TimeField(null=True, verbose_name='Start time', blank=True)),
                ('end_date', models.DateField(null=True, verbose_name='End date', blank=True)),
                ('end_time', models.TimeField(null=True, verbose_name='End time', blank=True)),
                ('url', models.CharField(max_length=255, null=True, verbose_name='Signup URL', blank=True)),
                ('location', models.CharField(max_length=255, null=True, blank=True)),
                ('address', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', django_extensions.db.fields.AutoSlugField(allow_duplicates=False, separator=b'"u\'-\'"', blank=True, populate_from=b'"\'title\'"', editable=False, verbose_name='slug', overwrite=False)),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
                ('url', models.CharField(max_length=255)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', django_extensions.db.fields.AutoSlugField(allow_duplicates=False, separator=b'"u\'-\'"', blank=True, populate_from=b'"\'title\'"', editable=False, verbose_name='slug', overwrite=False)),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
                ('public_url', models.CharField(max_length=255, null=True, blank=True)),
                ('dev_url', models.CharField(max_length=255, null=True, blank=True)),
                ('git_url', models.CharField(max_length=255, null=True, blank=True)),
                ('status', models.CharField(default=b'ideation', max_length=10, choices=[(b'inprogress', b'In Progress'), (b'ideation', b'Ideation'), (b'stalled', b'Stalled'), (b'defunct', b'Defunct'), (b'launched', b'Launched')])),
                ('color', models.CharField(max_length=100, null=True, verbose_name='Color', blank=True)),
                ('screenshot', models.ImageField(upload_to=b'screenshots', null=True, verbose_name='Screenshot', blank=True)),
                ('events', models.ManyToManyField(to='honey.Event', null=True, blank=True)),
                ('founder', models.ForeignKey(related_name='founder', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, blank=True)),
            ],
            options={
                'ordering': ['-created'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectCommit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('chash', models.CharField(max_length=255)),
                ('message', models.TextField(null=True, blank=True)),
                ('summary', models.TextField(null=True, blank=True)),
                ('string_author', models.CharField(max_length=255, null=True, blank=True)),
                ('time', models.DateTimeField(null=True, blank=True)),
                ('diff', models.TextField(null=True, blank=True)),
                ('project', models.ForeignKey(to='honey.Project')),
                ('user_author', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['-created'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectIdea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('slug', django_extensions.db.fields.ShortUUIDField(max_length=36, editable=False, blank=True)),
                ('started_date', models.DateTimeField(null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='created_by', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_votes', models.ManyToManyField(related_name='user_votes', null=True, to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
                'ordering': ['-created'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', django_extensions.db.fields.AutoSlugField(allow_duplicates=False, separator=b'"u\'-\'"', blank=True, populate_from=b'"\'title\'"', editable=False, verbose_name='slug', overwrite=False)),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
                ('pending', models.BooleanField(default=True)),
                ('project_count', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', django_extensions.db.fields.AutoSlugField(allow_duplicates=False, separator=b'"u\'-\'"', blank=True, populate_from=b'"\'title\'"', editable=False, verbose_name='slug', overwrite=False)),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
                ('pending', models.BooleanField(default=True)),
                ('project_count', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='projectcommit',
            unique_together=set([('project', 'chash')]),
        ),
        migrations.AddField(
            model_name='project',
            name='technologies',
            field=models.ManyToManyField(to='honey.Technology', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='topics',
            field=models.ManyToManyField(to='honey.Topic', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='link',
            name='project',
            field=models.ForeignKey(to='honey.Project'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='buzz',
            name='project',
            field=models.ForeignKey(to='honey.Project'),
            preserve_default=True,
        ),
    ]
