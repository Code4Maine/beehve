from django.core.urlresolvers import reverse
import floppyforms as forms
import select2.fields

from .models import Project, Topic, Event, Technology, Buzz


class BuzzForm(forms.ModelForm):
    class Meta:
        model = Buzz
        exclude = ['project', 'author']


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
                  'screenshot', 'github_url', 'topics', 'events', 
                  'technologies', 'color']


class TopicForm(forms.ModelForm):

    class Meta:
        model = Topic
        exclude = ['pending']


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        exclude = ['pending']


class TechnologyForm(forms.ModelForm):

    class Meta:
        model = Technology
        exclude = ['pending']
