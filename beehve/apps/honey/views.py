import json
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.views.generic import DetailView, ListView, View
from django.core import serializers
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string

from .models import Project, Topic, Technology, Event, Buzz
from .forms import ProjectForm, TopicForm, EventForm, TechnologyForm, BuzzForm
from .utils import send_email
from braces import views


class JsonView(views.CsrfExemptMixin,
               views.JsonRequestResponseMixin,
               views.JSONResponseMixin, View):
    pass


class BuzzListView(ListView):
    model = Buzz

    def get_context_data(self, *args, **kwargs):
        context = super(BuzzListView, self).get_context_data(*args, **kwargs)
        context['technologies'] = Technology.objects.all()
        context['topics'] = Topic.objects.all()
        context['events'] = Event.objects.all()

        return context



class BuzzCreateView(views.LoginRequiredMixin, CreateView):
    model = Buzz
    form_class = BuzzForm

    def get_success_url(self):
        project = Project.objects.get(slug=self.kwargs['slug'])
        return reverse('project-detail', args=(project.slug,))


    def form_valid(self, form):
        object = form.save(commit=False)
        object.project = Project.objects.get(slug=self.kwargs['slug'])
        object.author = self.request.user
        object.save()

        member_emails = [m.email for m in object.project.members.all()]
        send_email(
            self.request, 
            member_emails,
            'Someone is buzzing about {0} on Code 4 Maine'.format(object.project),
            'honey/buzz_email.txt')
        return super(BuzzCreateView, self).form_valid(form)


class BuzzDetailView(JsonView, DetailView):
    model = Buzz


class ProjectCreateView(views.LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm

    def form_valid(self, form):
        object = form.save(commit=False)
        object.founder = self.request.user
        object.save()
        object.members.add(self.request.user)
        object.save()
        return super(ProjectCreateView, self).form_valid(form)
    

class ProjectUpdateView(views.LoginRequiredMixin, UpdateView):
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


class ProjectJoinView(JsonView, views.LoginRequiredMixin):
    """ A view that checks the request object for an 
    authenticated user and, if found, adds them to the 
    project member group.
    """
    def get(self, request, *args, **kwargs):
        user = self.request.user
        html = ''
        fragments = {}
        success = False
        project = Project.objects.get(slug=kwargs['slug'])
        if user.is_authenticated() and not user in project.members.all():
            project.members.add(user)
            project.save()
            success = True
            html = "<p class='leave-button' ><a href='{0}' class='tiny button radius ajax alert' data-replace='.leave-button'><i class='fa fa-times'></i> Leave project</a></p>".format(reverse('project-leave', args=[project.slug]))
            fragments['.member-thumbs'] = render_to_string('honey/_member_list.html', {'members': project.members.all()})
        return self.render_json_response(
            {'user': user.username, 'html': html, 'fragments': fragments})



class ProjectLeaveView(JsonView, views.LoginRequiredMixin):
    """ A view that checks the request object for an 
    authenticated user and, if found, adds them to the 
    project member group.
    """
    def get(self, request, *args, **kwargs):
        user = self.request.user
        html = ''
        fragments = {}
        success = False
        project = Project.objects.get(slug=kwargs['slug'])
        if user.is_authenticated() and user in project.members.all():
            project.members.remove(user)
            project.save()
            html = "<p class='join-button' ><a href='{0}' class='tiny button radius ajax success' data-replace='.join-button'><i class='fa fa-plus'></i> Join project</a></p>".format(reverse('project-join', args=[project.slug]))
            success = True
            fragments['.member-thumbs'] = render_to_string('honey/_member_list.html', {'members': project.members.all()})
        return self.render_json_response(
            {'user': user.username, 'html': html, 'fragments': fragments})


class ProjectListView(JsonView, ListView):
    model = Project
    form_class = ProjectForm


class TechnologyDetailView(DetailView):
    model = Technology


class TechnologyListView(ListView):
    model = Technology


class TechnologyCreateView(views.LoginRequiredMixin, CreateView):
    model = Technology
    form_class = TechnologyForm

    def get_success_url(self, *args, **kwargs):
        redirect = getattr(self.request.GET, 'next', '/projects/add/')
        if redirect:
            return redirect


class TopicCreateView(views.LoginRequiredMixin, CreateView):
    model = Topic
    form_class = TopicForm

    def get_success_url(self, *args, **kwargs):
        redirect = getattr(self.request.GET, 'next', '/projects/add/')
        if redirect:
            return redirect

class TopicDetailView(DetailView):
    model = Topic


class TopicListView(ListView):
    model = Topic


class EventDetailView(DetailView):
    model = Event


class EventListView(ListView):
    model = Event


class EventCreateView(views.LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventForm

    def get_success_url(self, *args, **kwargs):
        redirect = getattr(self.request.GET, 'next', '/projects/add/')
        if redirect:
            return redirect

