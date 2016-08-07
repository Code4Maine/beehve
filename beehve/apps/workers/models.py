from django.conf import settings
from django.db import models
from localflavor.us.models import PhoneNumberField
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel, TitleSlugDescriptionModel
from homepage.models import Brigade


class Position(TitleSlugDescriptionModel, TimeStampedModel):
    order = models.IntegerField(_('Order'), default=0)
    brigade = models.ForeignKey(Brigade)

    class Meta:
        ordering = ('order',)

    @models.permalink
    def get_absolute_url(self):
        return ('position-detail', None, {'slug': self.slug})

    def __unicode__(self):
        return '{0} {1}'.format(self.brigade, self.title)


class Worker(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(_('Name'), max_length=255, blank=True, null=True)
    why = models.TextField(_('Why I am part of Code 4 Maine'), blank=True, null=True)
    website = models.CharField(_('Personal website'), max_length=200, blank=True, null=True)
    phone = models.CharField(_('Phone'), max_length=20, blank=True, null=True)
    city = models.CharField(_('City'), max_length=100, blank=True, null=True)
    skype = models.CharField(_('Skype username'), max_length=100, blank=True, null=True)
    github = models.CharField(_('Github username'), max_length=100, blank=True, null=True)
    twitter = models.CharField(_('Twitter username'), max_length=100, blank=True, null=True)
    facebook = models.CharField(_('Facebook username'), max_length=100, blank=True, null=True)
    instagram = models.CharField(_('Instagram username'), max_length=100, blank=True, null=True)
    linkedin = models.CharField(_('LinkedIn username'), max_length=100, blank=True, null=True)
    email_notify = models.BooleanField(_('Email notifications on updates'), default=True)
    position = models.ForeignKey(Position, blank=True, null=True)
    active = models.BooleanField(_('Is worker active?'), default=True)


    @models.permalink
    def get_absolute_url(self):
        return ('worker-detail', None, {'slug': self.user.username})

    def __unicode__(self):
        if self.name:
            return '{0}'.format(self.name)
        else:
            return '{0}'.format(self.user)
