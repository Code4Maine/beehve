from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import (TitleSlugDescriptionModel,
                                         TimeStampedModel)
from django.contrib.auth import get_user_model


class BasicItem(TimeStampedModel, TitleSlugDescriptionModel):
    pending = models.BooleanField(default=True)
    project_count = models.IntegerField(default=0)

    class Meta:
        abstract = True

    def __unicode__(self):
        return u'{0}'.format(self.title)

    def save(self, *args, **kwargs):
        try:
            self.project_count = len(self.project_set.all())
        except:
            pass
        super(BasicItem, self).save(*args, **kwargs)



class Topic(BasicItem):

    @models.permalink
    def get_absolute_url(self):
        return ('topic-detail', None, {'slug': self.slug})


class Event(BasicItem):

    @models.permalink
    def get_absolute_url(self):
        return ('event-detail', None, {'slug': self.slug})


class Technology(BasicItem):

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
    topics = models.ManyToManyField(Topic, blank=True, null=True)
    events = models.ManyToManyField(Event, blank=True, null=True)
    technologies = models.ManyToManyField(Technology, blank=True, null=True)
    members = models.ManyToManyField(get_user_model(), blank=True, null=True)
    founder = models.ForeignKey(get_user_model(), blank=True, null=True, 
        related_name="founder")
    status = models.CharField(
        max_length=10, 
        choices=PROJECT_STATUSES, 
        default='active')
    color = models.CharField(_('Color'), max_length=100, blank=True, null=True)
    screenshot = models.ImageField(_('Screenshot'), blank=True, null=True,
                                   upload_to='screenshots')

    def __unicode__(self):
        return u'{0}'.format(self.title)

    @models.permalink
    def get_absolute_url(self):
        return ('project-detail', None, {'slug': self.slug})


class Buzz(TimeStampedModel, TitleSlugDescriptionModel):
    project = models.ForeignKey(Project)
    author = models.ForeignKey(get_user_model())
    
    def __unicode__(self):
        return u'{0}'.format(self.title)

    @models.permalink
    def get_absolute_url(self):
        return ('buzz-detail', None, {'project_slug': self.project.slug, 'slug': self.slug})


