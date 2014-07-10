from django.db import models
from localflavor.us.models import PhoneNumberField
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save


class Worker(TimeStampedModel):
    user = models.ForeignKey(get_user_model())
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


    @models.permalink
    def get_absolute_url(self):
        return ('worker-detail', None, {'slug': self.user.username})

    def __unicode__(self):
        return u'{0}'.format(self.name)

def get_or_create_worker(sender, instance, **kwargs):
    Worker.objects.get_or_create(user=instance)

post_save.connect(get_or_create_worker, sender=get_user_model(), dispatch_uid='get_or_create_worker')
get_user_model().worker = property(lambda u: Worker.objects.get_or_create(user=u)[0])
