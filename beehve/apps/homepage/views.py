from datetime import datetime, timedelta
from django.utils import timezone
from itertools import chain
from django.conf import settings
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.views.generic import DetailView, ListView, View
from django.core import serializers
from django.core.urlresolvers import reverse

from .models import Partner, Initiative, Brigade
from .forms import PartnerForm
from braces import views

from honey.models import Technology, Topic, Event, Project, ProjectCommit, Buzz
from workers.models import Worker

class HomepageView(ListView):
    model = Brigade
    template_name = 'homepage.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomepageView, self).get_context_data(*args, **kwargs)
        # TODO: Get the brigade that's indicated in the subdomain
        try:
            context['brigade'] = Brigade.objects.filter(active=True)[0]
        except:
            context['brigade'] = None

        context['initiatives'] = Initiative.objects.filter(brigade=context['brigade'],
                                                          active=True)
        context['partners'] = Partner.objects.filter(brigade=context['brigade'],
                                                          active=True)

        context['technologies'] = Technology.objects.all()
        context['topics'] = Topic.objects.all()
        context['events'] = Event.objects.all()
        context['projects'] = Project.objects.all()
        context['workers'] = Worker.objects.all()
        # zipper together all the commits and buzzes into a list 
        # sorted by created time
        now = timezone.now()
        context['commit_days'] = commits_since = getattr(settings, 'HONEY_COMMITS_SINCE_DAYS', 14)
        since = now - timedelta(days=commits_since)
        context['commits'] = ProjectCommit.objects.filter(created__gte=since)
        context['buzzes'] = Buzz.objects.all()
        if context['buzzes'] and context['commits']:
            context['updates'] = sorted(
                chain(context['buzzes'], context['commits']),
                key=lambda instance: instance.created, reverse=True)

        return context


class JsonView(views.CsrfExemptMixin,
               views.JsonRequestResponseMixin,
               views.JSONResponseMixin, View):
    pass


class PartnerListJSONView(JsonView, ListView):
    model = Partner
    json_dumps_kwargs = {"indent": 2}
    queryset = Partner.objects.filter(active=True)

    def get(self, request, *args, **kwargs):
        context = serializers.serialize('json',
                                        self.get_queryset().all())

        return self.render_json_response(context)


class PartnerDetailView(DetailView):
    model = Partner
    queryset = Partner.objects.filter(active=True)


class PartnerListView(ListView):
    model = Partner
    queryset = Partner.objects.filter(active=True)


class PartnerUpdateView(UpdateView):
    model = Partner
    form_class = PartnerForm
    queryset = Partner.objects.filter(active=True)

    def get_success_url(self):
        return reverse('partner-detail')


class InitiativeListJSONView(JsonView, ListView):
    model = Initiative
    json_dumps_kwargs = {"indent": 2}
    queryset = Initiative.objects.filter(active=True)

    def get(self, request, *args, **kwargs):
        context = serializers.serialize('json',
                                        self.get_queryset().all())

        return self.render_json_response(context)


class InitiativeDetailView(DetailView):
    model = Initiative
    queryset = Initiative.objects.filter(active=True)


class InitiativeListView(ListView):
    model = Initiative
    queryset = Initiative.objects.filter(active=True)
