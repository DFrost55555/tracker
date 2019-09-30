from django import forms
from .models import Project
from apps.customers.models import Customer
from django.forms import ModelChoiceField

CHARGE_CODE_CHOICES = (
    ('wbs','WBS Code'),
    ('ctr', 'Cost Centre'),
    ('trs','MARS Request')
)

STATUS_CHOICES = (
    ('active','Active'),
    ('inactive','Inactive'),
    ('onhold','On Hold'),
    ('archive','Archive'),
)

class ProjectModelForm(forms.ModelForm):
    project_name = forms.CharField(widget=forms.TextInput(), required=True)
    project_customer_fk = ModelChoiceField(queryset=Customer.objects.all(), initial=0, required=True)
    project_reference = forms.CharField(widget=forms.TextInput(), required=True)
    project_chargecode = forms.CharField(widget=forms.TextInput(), required=True)
    project_chargecodetype = forms.CharField(widget=forms.Select(choices=CHARGE_CODE_CHOICES))
    project_status = forms.CharField(widget=forms.Select(choices=STATUS_CHOICES))
    
    class Meta:
        model = Project
        fields = [
            "project_name",
            "project_customer_fk",
            "project_reference",
            "project_chargecode",
            "project_chargecodetype",
            "project_status",
            
        ]
        