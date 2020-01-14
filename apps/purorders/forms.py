from django import forms
from .models import PurchaseOrder, POStatus, POType, PONote, POMatrix, POFiles
from apps.customers.models import Customer
from apps.suppliers.models import Supplier, SupplierStatus
from apps.projects.models import Project
from django.forms import ModelChoiceField, CharField, DecimalField, NumberInput
from djmoney.models.fields import MoneyField

class DatePicker(forms.DateInput):
    input_type = 'date'

class PurOrderModelForm(forms.ModelForm):
    po_reference = forms.CharField(label="PO Reference", widget=forms.TextInput(), required=True)
    po_quantity = forms.DecimalField(label="Quantity", widget=forms.NumberInput(), required=True)
    po_quantity_type_fk = ModelChoiceField(label="Quantity Type", queryset=POType.objects.all(), initial=0, required=True)
    po_cost_value = MoneyField(label="Cost Value", max_digits=14, decimal_places=2, null=True, default_currency='GBP')
    po_unit_cost = MoneyField(label="Unit Cost", max_digits=14, decimal_places=2, null=True, default_currency='GBP')
    po_charge_value = MoneyField(label="Charges Value", max_digits=14, decimal_places=2, null=True, default_currency='GBP')
    po_unit_charge = MoneyField(label="Unit Charge", max_digits=14, decimal_places=2, null=True, default_currency='GBP')
    po_start_date = forms.DateField(label='Start Date', widget=DatePicker(), required=False)
    po_end_date = forms.DateField(label='End Date', widget=DatePicker(), required=False)
    po_status_fk = ModelChoiceField(label="Status", queryset=POStatus.objects.all(), initial=0, required=True)


    class Meta:
        model = PurchaseOrder
        fields = [
            "po_reference",
            "po_quantity",
            "po_quantity_type_fk",
            "po_cost_value",
            "po_unit_cost",
            "po_charge_value",
            "po_unit_charge",
            "po_start_date",
            "po_end_date",
            "po_status_fk",
        ]
