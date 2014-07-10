from django.core.urlresolvers import reverse
import floppyforms as forms
import select2.fields

from .models import Project, Topic, Event, Technology, Buzz


class BuzzForm(forms.ModelForm):
    class Meta:
        model = Buzz
        exclude = ['project', 'author']


class ProjectForm(forms.ModelForm):
    topics = forms.ModelMultipleChoiceField(
        queryset=Topic.objects.all(),
        widget=forms.SelectMultiple(
            attrs={'inline': True, 'class': 'multiselect',}),
        required=False)
    events = forms.ModelMultipleChoiceField(
        queryset=Event.objects.all(),
        widget=forms.SelectMultiple(
            attrs={'inline': True, 'class': 'multiselect',}),
        required=False)
    technologies = forms.ModelMultipleChoiceField(
        queryset=Technology.objects.all(),
        widget=forms.SelectMultiple(
            attrs={'inline': True, 'class': 'multiselect',}),
        required=False)
    color = forms.CharField(
        widget=forms.TextInput(
            attrs={'inline': True, 'class': 'colorpicker',}),
        required=False)

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
