from django.template import RequestContext

from .models import Project, Technology, Topic, Event
from django.contrib.auth import get_user_model

def menu_preloader(request):
    workers = get_user_model().objects.all()
    projects = Project.objects.all()
    technologies = Technology.objects.all()
    topics = Topic.objects.all()
    events = Event.objects.all()
    return {'projects': projects, 
            'technologies': technologies, 
            'topics': topics, 
            'events': events, 
            'workers': workers}
