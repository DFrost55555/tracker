from django import forms
#from django.contrib.admin.widgets import AdminDateWidget
#from bootstrap_datepicker_plus import DatePickerInput
from django.forms import ModelChoiceField
#from bootstrap_datepicker.widgets import DatePicker
from .models import Hardware, HardwareContact, HardwareNote, PortfolioStatus
from apps.lists.models import ProductType,HardwareCategory, HardwareStatus, YesNo
from apps.customers.models import Customer
from apps.vendors.models import Vendor

class DatePicker(forms.DateInput):
    input_type = 'date'


class HardwareModelForm(forms.ModelForm):
    hw_description = forms.CharField(label='Hardware Description', widget=forms.TextInput(), required=True)
    hw_vend_fk = ModelChoiceField(label='Vendor', queryset=Vendor.objects.all().order_by('vend_name'), initial=0, required=True)
    hw_repl_desc = forms.CharField(label='Replacement Hardware Description', widget=forms.TextInput(), required=False)
    hw_repl_vend_fk = ModelChoiceField(label='Replacement Hardware Vendor', queryset=Vendor.objects.all().order_by('vend_name'), initial=0, required=False)
    hw_cust_fk = ModelChoiceField(label='Customer', queryset=Customer.objects.all().order_by('cust_name'), initial=0, required=False)
    hw_portsts_fk = ModelChoiceField(label='Portfolio Status', queryset=PortfolioStatus.objects.all(), initial=0, required=False)
    hw_hwcat_fk = ModelChoiceField(label='Hardware Category', queryset=HardwareCategory.objects.all().order_by('hwcat_name'), initial=0, required=False)
    hw_hwsts_fk = ModelChoiceField(label='Hardware Status', queryset=HardwareStatus.objects.all(), initial=0, required=False)
    hw_int_code = forms.CharField(label='Internal Part Code', widget=forms.TextInput(), required=False)
    hw_ext_code = forms.CharField(label='External Part Code', widget=forms.TextInput(), required=False)
    hw_eol_date = forms.DateField(label='End of Life', widget=DatePicker(), required=False) # End of Life
    hw_eow_date = forms.DateField(label='End of Warranty', widget=DatePicker(), required=False) # End of Warranty
    hw_ems_date = forms.DateField(label='End of Mainstream Support', widget=DatePicker(), required=False) # End of Mainstream Support
    hw_ees1_date = forms.DateField(label='End of Extended Support - Period 1', widget=DatePicker(), required=False) # End of Extended Support - Period One
    hw_ees2_date = forms.DateField(label='End of Extended Support - Period 2', widget=DatePicker(), required=False) # End of Extended Support - Period Two
    hw_ees3_date = forms.DateField(label='End of Extended Support - Period 3', widget=DatePicker(), required=False) # End of Extended Support - Period Three
    hw_see_yn_fk = forms.ModelChoiceField(label='Support End Estimated', queryset=YesNo.objects.all().order_by('yesno_id'), initial=2, required=False) # Support End Estimated
    hw_plp_txt = forms.CharField(label='Product Lifecycle Policy', widget=forms.TextInput(), required=False) # Product Lifecycle Policy
    hw_upd_date = forms.DateField(label='Information Updated', widget=DatePicker(), required=False)
    hw_int_reference = forms.CharField(label='Internal Process Reference', widget=forms.TextInput(), required=False)

    class Meta:
        model = Hardware
        fields = [
            "hw_description",
            "hw_vend_fk",        
            "hw_repl_desc",
            "hw_repl_vend_fk",
            "hw_cust_fk",
            "hw_portsts_fk",
            "hw_hwcat_fk",
            "hw_hwsts_fk",
            "hw_int_code",
            "hw_ext_code",
            "hw_eol_date",
            "hw_eow_date",
            "hw_ems_date",
            "hw_ees1_date",
            "hw_ees2_date",
            "hw_ees3_date",
            "hw_see_yn_fk",
            "hw_plp_txt",
            "hw_upd_date",
            "hw_int_reference",
        ]