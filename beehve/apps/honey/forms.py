from django.core.urlresolvers import reverse
import floppyforms as forms
import select2.fields

from .models import Project, Topic, Event, Technology


class ProjectForm(forms.ModelForm):
    topics = select2.fields.MultipleChoiceField(
        choices=Topic.objects.as_choices(),
        overlay="Choose topics ...")
    events = select2.fields.MultipleChoiceField(
        choices=Event.objects.as_choices(),
        overlay="Choose events ...")
    technologies = select2.fields.MultipleChoiceField(
        choices=Technology.objects.as_choices(),
        overlay="Choose technologies ...")

    class Meta:
        model = Project
        fields = ['title', 'description', 'public_url', 'dev_url',
                  'github_url', 'topics', 'events', 'technologies']
