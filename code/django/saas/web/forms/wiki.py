from django import forms
from web.forms.bootstrap import BootstrapForm
from web import models

class WikiModelForm(BootstrapForm, forms.ModelForm):
    class Meta:
        model = models.Wiki
        exclude = ['project',]