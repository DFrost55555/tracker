from django import forms
from .models import Project, POStatus, POType, PONote, POMatrix, POFiles
from apps.customers.models import Customer
from apps.suppliers.models import Supplier, SupplierStatus
from apps.projects.models import Project
from django.forms import ModelChoiceField
from djmoney.models.fields import MoneyField

class PurOrderModelForm(forms.ModelForm):
    po_reference = forms.CharField(widget=forms.TextInput(), required=True)
    
    project_customer_fk = ModelChoiceField(queryset=Customer.objects.all(), initial=0, required=True)
    project_reference = forms.CharField(widget=forms.TextInput(), required=True)
    project_chargecode = forms.CharField(widget=forms.TextInput(), required=True)
    project_chargecodetype_fk = ModelChoiceField(queryset=ChargeCodeType.objects.all(), initial=0, required=True)
    project_statustype_fk = ModelChoiceField(queryset=ProjectStatus.objects.all(), initial=0, required=True)

    class Meta:
        model = Project
        fields = [
            "po_reference",
            "project_customer_fk",
            "project_reference",
            "project_chargecode",
            "project_chargecodetype_fk",
            "project_statustype_fk",
        ]


class CustProjectModelForm(forms.ModelForm):
    project_name = forms.CharField(widget=forms.TextInput(), required=True)
    project_customer_fk = ModelChoiceField(widget=forms.HiddenInput(), queryset=Customer.objects.all(), initial=0, required=True)
    project_reference = forms.CharField(widget=forms.TextInput(), required=True)
    project_chargecode = forms.CharField(widget=forms.TextInput(), required=True)
    #project_chargecodetype_fk = ModelChoiceField(queryset=ChargeCodeType.objects.all(), initial=1, required=False)
    #project_statustype_fk = ModelChoiceField(queryset=ProjectStatus.objects.all(), initial=1, required=False)

    class Meta:
        model = Project
        fields = [
            "project_name",
            "project_customer_fk",
            "project_reference",
            "project_chargecode",
            #"project_chargecodetype_fk",
            #"project_statustype_fk",
        ]