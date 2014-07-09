from django.template import RequestContext

from .models import Project
from django.contrib.auth import get_user_model

def menu_preloader(request):
    workers = get_user_model().objects.all()
    projects = Project.objects.all()
    return {'projects': projects, 'workers': workers}
