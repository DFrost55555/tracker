from django import forms
from .models import PurchaseOrder, POStatus, POType, PONote, POMatrix, POFiles
from apps.customers.models import Customer
from apps.suppliers.models import Supplier, SupplierStatus
from apps.projects.models import Project
from django.forms import ModelChoiceField
#from djmoney.models.fields import MoneyField
#from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Layout, Submit, Row, Column


class DateInput(forms.DateInput):
    input_type = 'date'
    

class PurOrderModelForm(forms.ModelForm):
    po_reference = forms.CharField(widget=forms.TextInput(), required=True)
    po_quantity = forms.DecimalField(widget=forms.NumberInput(), required=True)
    po_quantity_type_fk = ModelChoiceField(queryset=POType.objects.all(), initial=0, required=True)
    po_cost_value = forms.DecimalField(max_digits=14, decimal_places=2, localize=True)
    po_unit_cost = forms.DecimalField(max_digits=14, decimal_places=2)
    po_charge_value = forms.DecimalField(max_digits=14, decimal_places=2)
    po_unit_charge = forms.DecimalField(max_digits=14, decimal_places=2)
    po_start_date = forms.DateField(widget=DateInput, required=True)
    po_end_date = forms.DateField(widget=DateInput, required=True)
    po_status_fk = ModelChoiceField(queryset=POStatus.objects.all(), initial=0, required=True)
    
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
