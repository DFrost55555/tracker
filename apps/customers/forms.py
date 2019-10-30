from django import forms
from .models import Customer
from apps.projects.models import Project
from apps.statustype.models import StatusType
from apps.chgcodetype.models import ChgCodeType
from django.forms import ModelChoiceField, HiddenInput


class CustProjectModelForm(forms.ModelForm):
    project_name = forms.CharField(widget=forms.TextInput(), required=True)
    project_customer_fk = forms.CharField(widget=forms.HiddenInput())
    project_reference = forms.CharField(widget=forms.TextInput(), required=True)
    project_chargecode = forms.CharField(widget=forms.TextInput(), required=True)
    project_chargecodetype_fk = ModelChoiceField(queryset=ChgCodeType.objects.all(), initial=0, required=True)
    project_statustype_fk = ModelChoiceField(queryset=StatusType.objects.all(), initial=0, required=True)

    class Meta:
        model = Project
        fields = [
            "project_name",
            "project_customer_fk",
            "project_reference",
            "project_chargecode",
            "project_chargecodetype_fk",
            "project_statustype_fk",
        ]