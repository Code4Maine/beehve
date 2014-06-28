from django.core.urlresolvers import reverse
import floppyforms as forms
from .models import Project


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
