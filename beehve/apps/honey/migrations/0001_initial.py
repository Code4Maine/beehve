# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BasicItem'
        db.create_table(u'honey_basicitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django_extensions.db.fields.AutoSlugField')(allow_duplicates=False, max_length=50, separator=u'-', blank=True, populate_from='title', overwrite=False)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'honey', ['BasicItem'])

        # Adding model 'Topic'
        db.create_table(u'honey_topic', (
            (u'basicitem_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['honey.BasicItem'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'honey', ['Topic'])

        # Adding model 'Event'
        db.create_table(u'honey_event', (
            (u'basicitem_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['honey.BasicItem'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'honey', ['Event'])

        # Adding model 'Technology'
        db.create_table(u'honey_technology', (
            (u'basicitem_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['honey.BasicItem'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'honey', ['Technology'])

        # Adding model 'Project'
        db.create_table(u'honey_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django_extensions.db.fields.AutoSlugField')(allow_duplicates=False, max_length=50, separator=u'-', blank=True, populate_from='title', overwrite=False)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('public_url', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('dev_url', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('github_url', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='active', max_length=10)),
        ))
        db.send_create_signal(u'honey', ['Project'])

        # Adding M2M table for field topics on 'Project'
        m2m_table_name = db.shorten_name(u'honey_project_topics')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'honey.project'], null=False)),
            ('topic', models.ForeignKey(orm[u'honey.topic'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'topic_id'])

        # Adding M2M table for field events on 'Project'
        m2m_table_name = db.shorten_name(u'honey_project_events')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'honey.project'], null=False)),
            ('event', models.ForeignKey(orm[u'honey.event'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'event_id'])

        # Adding M2M table for field technologies on 'Project'
        m2m_table_name = db.shorten_name(u'honey_project_technologies')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'honey.project'], null=False)),
            ('technology', models.ForeignKey(orm[u'honey.technology'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'technology_id'])

        # Adding M2M table for field members on 'Project'
        m2m_table_name = db.shorten_name(u'honey_project_members')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'honey.project'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'user_id'])


    def backwards(self, orm):
        # Deleting model 'BasicItem'
        db.delete_table(u'honey_basicitem')

        # Deleting model 'Topic'
        db.delete_table(u'honey_topic')

        # Deleting model 'Event'
        db.delete_table(u'honey_event')

        # Deleting model 'Technology'
        db.delete_table(u'honey_technology')

        # Deleting model 'Project'
        db.delete_table(u'honey_project')

        # Removing M2M table for field topics on 'Project'
        db.delete_table(db.shorten_name(u'honey_project_topics'))

        # Removing M2M table for field events on 'Project'
        db.delete_table(db.shorten_name(u'honey_project_events'))

        # Removing M2M table for field technologies on 'Project'
        db.delete_table(db.shorten_name(u'honey_project_technologies'))

        # Removing M2M table for field members on 'Project'
        db.delete_table(db.shorten_name(u'honey_project_members'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'honey.basicitem': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'BasicItem'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'populate_from': "'title'", 'overwrite': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'honey.event': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Event', '_ormbases': [u'honey.BasicItem']},
            u'basicitem_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['honey.BasicItem']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'honey.project': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Project'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'dev_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'events': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['honey.Event']", 'null': 'True', 'blank': 'True'}),
            'github_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'public_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'populate_from': "'title'", 'overwrite': 'False'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'active'", 'max_length': '10'}),
            'technologies': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['honey.Technology']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'topics': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['honey.Topic']", 'null': 'True', 'blank': 'True'})
        },
        u'honey.technology': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Technology', '_ormbases': [u'honey.BasicItem']},
            u'basicitem_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['honey.BasicItem']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'honey.topic': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Topic', '_ormbases': [u'honey.BasicItem']},
            u'basicitem_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['honey.BasicItem']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['honey']