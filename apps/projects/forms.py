from django import forms
from .models import Project
from apps.customers.models import Customer
from apps.statustype.models import StatusType
from django.forms import ModelChoiceField

CHARGE_CODE_CHOICES = (
    ('wbs','WBS Code'),
    ('ctr', 'Cost Centre'),
    ('trs','MARS Request')
)


class ProjectModelForm(forms.ModelForm):
    project_name = forms.CharField(widget=forms.TextInput(), required=True)
    project_customer_fk = ModelChoiceField(queryset=Customer.objects.all(), initial=0, required=True)
    project_reference = forms.CharField(widget=forms.TextInput(), required=True)
    project_chargecode = forms.CharField(widget=forms.TextInput(), required=True)
    project_chargecodetype = forms.CharField(widget=forms.Select(choices=CHARGE_CODE_CHOICES))
    project_status_fk = ModelChoiceField(queryset=StatusType.objects.all(), initial=0, required=True
    
    class Meta:
        model = Project
        fields = [
            "project_name",
            "project_customer_fk",
            "project_reference",
            "project_chargecode",
            "project_chargecodetype",
            "project_status_fk",
            
        ]
        