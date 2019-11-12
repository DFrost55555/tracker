from django import forms
from bootstrap_datepicker_plus import DatePickerInput
from django.forms import ModelChoiceField

from .models import Hardware, HardwareContact, HardwareNote, PortfolioStatus
from apps.lists.models import ProductType,HardwareCategory,HardwareStatus
from apps.customers.models import Customer
from apps.vendors.models import Vendor


class HardwareModelForm(forms.ModelForm):
    # hw_description = forms.CharField(widget=forms.TextInput(), required=True)
    # hw_vend_fk = ModelChoiceField(queryset=Vendor.objects.all(), initial=0, required=True)
    # hw_repl_desc = forms.CharField(widget=forms.TextInput(), required=False)
    # hw_repl_vend_fk = ModelChoiceField(queryset=Vendor.objects.all(), initial=0, required=False)
    # hw_cust_fk = ModelChoiceField(queryset=Customer.objects.all(), initial=0, required=False)
    # hw_portsts_fk = ModelChoiceField(queryset=PortfolioStatus.objects.all(), initial=0, required=False)
    # hw_hwcat_fk = ModelChoiceField(queryset=HardwareCategory.objects.all(), initial=0, required=False)
    # hw_hwsts_fk = ModelChoiceField(queryset=HardwareStatus.objects.all(), initial=0, required=False)
    # hw_int_code = forms.CharField(widget=forms.TextInput(), required=False)
    # hw_ext_code = forms.CharField(widget=forms.TextInput(), required=False)
    # hw_eol_date = forms.DateField(widget=DatePickerInput(options={"format": "dd/mm/yyy", "autoclose": True})) # End of Life
    # hw_eow_date = forms.DateField(widget=DatePickerInput(options={"format": "dd/mm/yyy", "autoclose": True})) # End of Warranty
    # hw_ems_date = forms.DateField(widget=DatePickerInput(options={"format": "dd/mm/yyy", "autoclose": True})) # End of Mainstream Support
    # hw_ees1_date = forms.DateField(widget=DatePickerInput(options={"format": "dd/mm/yyy", "autoclose": True})) # End of Extended Support - Period One
    # hw_ees2_date = forms.DateField(widget=DatePickerInput(options={"format": "dd/mm/yyy", "autoclose": True})) # End of Extended Support - Period Two
    # hw_ees3_date = forms.DateField(widget=DatePickerInput(options={"format": "dd/mm/yyy", "autoclose": True})) # End of Extended Support - Period Three
    # hw_see_txt = forms.CharField(widget=forms.TextInput(), required=False) # Support End Estimated
    # hw_plp_txt = forms.CharField(widget=forms.TextInput(), required=False) # Product Lifecycle Policy
    # hw_upd_date = forms.DateField(widget=DatePickerInput(options={"format": "dd/mm/yyy", "autoclose": True}))
    # hw_int_reference = forms.CharField(widget=forms.TextInput(), required=False)

    class Meta:
        model = Hardware
        fields = ['hw_description',
                  'hw_vend_fk',
                  'hw_repl_desc',
                  'hw_repl_vend_fk',
                  'hw_cust_fk',
                  'hw_portsts_fk',
                  'hw_hwcat_fk',
                  'hw_hwsts_fk',
                  'hw_int_code',
                  'hw_ext_code',
                  'hw_eol_date',
                  'hw_eow_date',
                  'hw_ems_date',
                  'hw_ees1_date',
                  'hw_ees2_date',
                  'hw_ees3_date',
                  'hw_see_txt',
                  'hw_plp_txt',
                  'hw_upd_date',
                  'hw_int_reference',
                  ]
