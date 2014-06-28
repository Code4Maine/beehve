from django.views.generic.edit import CreateView, UpdateView, FormView
from django.views.generic import DetailView, ListView, View
from django.core import serializers
from .forms import ProjectForm 

from .models import Project, Topic, Technology, Event
from braces import views


class JsonView(views.CsrfExemptMixin,
               views.JsonRequestResponseMixin,
               views.JSONResponseMixin, View):
    pass


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm


class ProjectDetailView(JsonView, DetailView):
    model = Project


class ProjectListJSONView(JsonView, ListView):
    model = Project
    json_dumps_kwargs = {u"indent": 2}

    def get(self, request, *args, **kwargs):
        context = serializers.serialize('json',
                                        self.get_queryset().all())

        return self.render_json_response(context)


class ProjectListView(JsonView, ListView):
    model = Project
    form_class = ProjectForm


class TechnologyDetailView(DetailView):
    model = Technology


class TechnologyListView(ListView):
    model = Technology


class TopicDetailView(DetailView):
    model = Topic


class TopicListView(ListView):
    model = Topic


class EventDetailView(DetailView):
    model = Event


class EventListView(ListView):
    model = Event
