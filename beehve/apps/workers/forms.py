from django.core.urlresolvers import reverse
import floppyforms as forms
from .models import Worker


class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        exclude = ['user']


