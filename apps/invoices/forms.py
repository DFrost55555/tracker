from django import forms
from .models import Invoice, INVMatrix, INVStatus, INVType, INVNote
from apps.lists.models import POItemType, ChargeUnitType
from apps.customers.models import Customer
from apps.suppliers.models import Supplier, SupplierStatus
from apps.projects.models import Project
from django.forms import ModelChoiceField
from bootstrap_datepicker_plus import DatePickerInput  

class DatePicker(forms.DateInput):
    input_type = 'date'
    

class InvoiceModelForm(forms.ModelForm):
    inv_quantity = forms.DecimalField(label='Invoice Quantity', max_digits=6, decimal_places=2)
    inv_quantity_type_fk = ModelChoiceField(label='Invoice Quantity Type', queryset=ChargeUnitType.objects.all(), initial=0, required=True)
    inv_cost_value = forms.DecimalField(label='Invoice Total Cost', max_digits=8, decimal_places=2)
    inv_unit_cost = forms.DecimalField(label='Invoice Unit Cost', max_digits=8, decimal_places=2)
    inv_chg_value = forms.DecimalField(label='Invoice Total Charge', max_digits=8, decimal_places=2)
    inv_unit_chg = forms.DecimalField(label='Invoice Unit Charge', max_digits=8, decimal_places=2)
    inv_date = forms.DateField(label='Invoice Date', widget=DatePickerInput(), required=True)
    inv_gr_reference = forms.CharField(label='GR Reference', widget=forms.TextInput(), required=True)
    inv_gr_date = forms.DateField(label='GR Date', widget=DatePickerInput(), required=True)
    
    class Meta:
        model = Invoice
        fields = [
            'inv_reference',
            'inv_quantity',
            'inv_quantity_type_fk',
            'inv_cost_value',
            'inv_unit_cost',
            'inv_date',
            'inv_gr_reference',
            'inv_gr_date',
        ]