from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import (TitleSlugDescriptionModel,
                                         TimeStampedModel)
from django_extensions.db.fields import ShortUUIDField


class BasicItem(TimeStampedModel, TitleSlugDescriptionModel):
    pending = models.BooleanField(default=True)
    project_count = models.IntegerField(default=0)

    class Meta:
        abstract = True

    def __unicode__(self):
        return '{0}'.format(self.title)

    def save(self, *args, **kwargs):
        super(BasicItem, self).save(*args, **kwargs)

        self.project_count = len(self.project_set.all())

        super(BasicItem, self).save(*args, **kwargs)



class Topic(BasicItem):

    @models.permalink
    def get_absolute_url(self):
        return ('topic-detail', None, {'slug': self.slug})


class Technology(BasicItem):

    @models.permalink
    def get_absolute_url(self):
        return ('technology-detail', None, {'slug': self.slug})


class Event(BasicItem):
    start_date = models.DateField(_('Start date'))
    start_time = models.TimeField(_('Start time'), blank=True, null=True)
    end_date = models.DateField(_('End date'), blank=True, null=True)
    end_time = models.TimeField(_('End time'), blank=True, null=True)
    url = models.CharField(_('Signup URL'), max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    @models.permalink
    def get_absolute_url(self):
        return ('topic-detail', None, {'slug': self.slug})


class HotIdeaManager(models.Manager):
    pass


class ColdIdeaManager(models.Manager):
    pass


class ProjectIdea(TimeStampedModel):
    title = models.CharField(_('Title'), max_length=255)
    description = models.TextField(_('Description'))
    slug = ShortUUIDField()
    user_votes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='user_votes')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True,
            null=True, related_name="created_by")
    started_date = models.DateTimeField(blank=True, null=True)

    objects = models.Manager()
    hot_objects = HotIdeaManager()
    cold_objects = ColdIdeaManager()

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return '{0}'.format(self.title)

    @models.permalink
    def get_absolute_url(self):
        return ('projectidea-detail', [], {'slug':self.slug})

    @property
    def started(self):
        if not self.started_date:
            return False
        else:
            return True


PROJECT_STATUSES = (('inprogress', 'In Progress'),
                    ('ideation', 'Ideation'),
                    ('stalled', 'Stalled'),
                    ('defunct', 'Defunct'),
                    ('launched', 'Launched'))


class Project(TimeStampedModel, TitleSlugDescriptionModel):
    public_url = models.CharField(max_length=255, blank=True, null=True)
    dev_url = models.CharField(max_length=255, blank=True, null=True)
    git_url = models.CharField(max_length=255, blank=True, null=True)
    topics = models.ManyToManyField(Topic)
    events = models.ManyToManyField(Event)
    technologies = models.ManyToManyField(Technology)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL)
    founder = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, 
        related_name="founder")
    status = models.CharField(
        max_length=10, 
        choices=PROJECT_STATUSES, 
        default='ideation')
    color = models.CharField(_('Color'), max_length=100, blank=True, null=True)
    screenshot = models.ImageField(_('Screenshot'), blank=True, null=True,
                                   upload_to='screenshots')

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return '{0}'.format(self.title)

    @models.permalink
    def get_absolute_url(self):
        return ('project-detail', None, {'slug': self.slug})

    def project_health(self):
        '''
        Project health is determined by a calculus of when things were last
        updated. This includes:

          - number of days since last Buzz
          - number of commits
          - number of unique commiters
          - number of days since last commit
          - stated project status
          - number of stated members
          - number of requests for help
        '''
        return 0


class Link(TimeStampedModel, TitleSlugDescriptionModel):
    project = models.ForeignKey(Project)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    url = models.CharField(max_length=255)

    def __unicode__(self):
        return '{0} ({1})'.format(self.title, self.url)


class ProjectCommit(TimeStampedModel):
    project = models.ForeignKey(Project)
    chash = models.CharField(max_length=255)
    message = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    string_author = models.CharField(max_length=255, blank=True, null=True)
    user_author = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    diff = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('project', 'chash')
        ordering = ['-created']

    def __unicode__(self):
        return 'Commit {0} in {1}'.format(self.chash[:15], self.project)

    @property
    def author(self):
        if self.user_author:
            return self.user_author
        else:
            return self.string_author

    @models.permalink
    def get_absolute_url(self):
        return ('commit-detail', None, {'project_slug': self.project.slug, 'slug': self.chash})


class Buzz(TimeStampedModel, TitleSlugDescriptionModel):
    project = models.ForeignKey(Project)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    
    def __unicode__(self):
        return '{0}'.format(self.title)

    @models.permalink
    def get_absolute_url(self):
        return ('buzz-detail', None, {'project_slug': self.project.slug, 'slug': self.slug})


