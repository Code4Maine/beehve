from django.core.urlresolvers import reverse
import floppyforms as forms
from .models import Partner, Initiative, Brigade


class BrigadeForm(forms.ModelForm):
    class Meta:
        model = Brigade
        exclude = []


class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        exclude = ['brigade']


class InitiativeForm(forms.ModelForm):
    class Meta:
        model = Initiative
        exclude = ['brigade']


