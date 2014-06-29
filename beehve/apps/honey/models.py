from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import (TitleSlugDescriptionModel,
                                         TimeStampedModel)
from django.contrib.auth import get_user_model
import select2.fields


class SelectManager(models.Manager):
    def as_choices(self):
        for object in self.all():
            yield (object.pk, unicode(object))


class BasicItem(TimeStampedModel, TitleSlugDescriptionModel):
    def __unicode__(self):
        return u'{0}'.format(self.title)


class Topic(BasicItem):
    objects = SelectManager()

    @models.permalink
    def get_absolute_url(self):
        return ('topic-detail', None, {'slug': self.slug})


class Event(BasicItem):
    objects = SelectManager()

    @models.permalink
    def get_absolute_url(self):
        return ('event-detail', None, {'slug': self.slug})


class Technology(BasicItem):
    objects = SelectManager()

    @models.permalink
    def get_absolute_url(self):
        return ('technology-detail', None, {'slug': self.slug})


class Event(BasicItem):
    location = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    @models.permalink
    def get_absolute_url(self):
        return ('topic-detail', None, {'slug': self.slug})

PROJECT_STATUSES = (('active', 'Active'),
                    ('inactive', 'Inactive'),
                    ('launched', 'Launched'))


class Project(TimeStampedModel, TitleSlugDescriptionModel):
    public_url = models.CharField(max_length=255, blank=True, null=True)
    dev_url = models.CharField(max_length=255, blank=True, null=True)
    github_url = models.CharField(max_length=255, blank=True, null=True)
    topics = select2.fields.ManyToManyField(Topic, blank=True, null=True)
    events = models.ManyToManyField(Event, blank=True, null=True)
    technologies = models.ManyToManyField(Technology, blank=True, null=True)
    members = models.ManyToManyField(get_user_model(), blank=True, null=True)
    founder = models.ForeignKey(get_user_model(), blank=True, null=True, 
        related_name="founder")
    status = models.CharField(
        max_length=10, 
        choices=PROJECT_STATUSES, 
        default='active')

    def __unicode__(self):
        return u'{0}'.format(self.title)

    @models.permalink
    def get_absolute_url(self):
        return ('project-detail', None, {'slug': self.slug})


