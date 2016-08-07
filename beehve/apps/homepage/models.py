from django.db import models
from localflavor.us.models import PhoneNumberField
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel, TitleSlugDescriptionModel
from django.db.models.signals import post_save

from honey.models import Project


class Brigade(TimeStampedModel, TitleSlugDescriptionModel):
    phone = models.CharField(_('Phone'), max_length=20, blank=True, null=True)
    meetup = models.CharField(_('Meetup link'), max_length=255, blank=True, null=True)
    chat = models.CharField(_('Chat link'), max_length=255, blank=True, null=True)
    github = models.CharField(_('Github link'), max_length=255, blank=True, null=True)

    twitter = models.CharField(_('Twitter username'), max_length=100, blank=True, null=True)
    facebook = models.CharField(_('Facebook username'), max_length=100, blank=True, null=True)
    instagram = models.CharField(_('Instagram username'), max_length=100, blank=True, null=True)
    background = models.CharField(_('Dashboard background color or URL'), 
                                  max_length=255, blank=True, null=True)
    active = models.BooleanField(_('Is brigade active?'), default=True)


    def __unicode__(self):
        return self.title

class Initiative(TimeStampedModel, TitleSlugDescriptionModel):
    brigade = models.ForeignKey(Brigade)
    area = models.CharField(_('Area'), max_length=255, blank=True, null=True,
        help_text='Examples: State-wide, Pilsen Neighborhood, etc.')
    year = models.CharField(_('Year'), max_length=4, blank=True, null=True)
    logo = models.ImageField(_('Logo'), upload_to='homepage/initiatives', blank=True, null=True)
    projects = models.ManyToManyField(Project)
    active = models.BooleanField(_('Is initiative active?'), default=True)

    @models.permalink
    def get_absolute_url(self):
        return ('initiative-detail', None, {'slug': self.slug})

    def __unicode__(self):
        return self.title


class Partner(TimeStampedModel, TitleSlugDescriptionModel):
    brigade = models.ForeignKey(Brigade)
    partner_type = models.CharField(_('Type'), max_length=255, blank=True, null=True)
    year = models.CharField(_('Year'), max_length=4, blank=True, null=True)
    logo = models.ImageField(_('Logo'), upload_to='homepage/partners', blank=True, null=True)
    projects = models.ManyToManyField(Project)

    from honey.models import Project
    active = models.BooleanField(_('Is partnership active?'), default=True)

    @models.permalink
    def get_absolute_url(self):
        return ('partner-detail', None, {'slug': self.slug})

    def __unicode__(self):
        return self.title
