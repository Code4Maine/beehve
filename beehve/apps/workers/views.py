from django.views.generic.edit import CreateView, UpdateView, FormView
from django.views.generic import DetailView, ListView, View
from django.core import serializers
from django.core.urlresolvers import reverse

from .models import Worker
from .forms import WorkerForm
from braces import views


class JsonView(views.CsrfExemptMixin,
               views.JsonRequestResponseMixin,
               views.JSONResponseMixin, View):
    pass


class WorkerListJSONView(JsonView, ListView):
    model = Worker
    json_dumps_kwargs = {u"indent": 2}

    def get(self, request, *args, **kwargs):
        context = serializers.serialize('json',
                                        self.get_queryset().all())

        return self.render_json_response(context)


class WorkerDetailView(DetailView):
    model = Worker
    slug_field = 'user__username'


class WorkerListView(ListView):
    model = Worker


class WorkerUpdateView(UpdateView):
    model = Worker
    form_class = WorkerForm

    def get_success_url(self):
        return reverse('profile-detail')

    def get_object(self, *args, **kwargs):
        return self.request.user.worker


class WorkerProfileView(DetailView):
    model = Worker

    def get_object(self, *args, **kwargs):
        return self.request.user

