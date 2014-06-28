from django.db import models
from localflavor.us.models import PhoneNumberField
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth import get_user_model


class Worker(TimeStampedModel):
    user = models.ForeignKey(get_user_model())
    phone = models.CharField(_('Phone'), max_length=20, blank=True, null=True)
    city = models.CharField(_('City'), max_length=100, blank=True, null=True)
    skype = models.CharField(_('Skype username'), max_length=100, blank=True, null=True)
    github = models.CharField(_('Github username'), max_length=100, blank=True, null=True)

    @models.permalink
    def get_absolute_url(self):
        return ('worker-detail', None, {'slug': self.user.username})
    
