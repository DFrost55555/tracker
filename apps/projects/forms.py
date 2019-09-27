from django import forms
from .models import Project
from tracker.apps.customers.models import Customer
from django.forms import ModelChoiceField


class ProjectModelForm(forms.ModelForm):
    project_name = forms.CharField(widget=forms.TextInput(), required=True)
    project_customer_fk = ModelChoiceField(queryset=Customer.objects.all(), initial=0, required=True)
    
    class Meta:
        model = Project
        fields = [
            "project_name",
            "project_customer_fk",
        ]
        