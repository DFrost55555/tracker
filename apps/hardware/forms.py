from django import forms
#from django.contrib.admin.widgets import AdminDateWidget
#from bootstrap_datepicker_plus import DatePickerInput
from django.forms import ModelChoiceField
#from bootstrap_datepicker.widgets import DatePicker
from .models import Hardware, HardwareContact, HardwareNote, PortfolioStatus
from apps.lists.models import ProductType,HardwareCategory,HardwareStatus
from apps.customers.models import Customer
from apps.vendors.models import Vendor

class DatePicker(forms.DateInput):
    input_type = 'date'


class HardwareModelForm(forms.ModelForm):
    hw_description = forms.CharField(widget=forms.TextInput(), required=True)
    hw_vend_fk = ModelChoiceField(queryset=Vendor.objects.all().order_by('vend_name'), initial=0, required=True)
    hw_repl_desc = forms.CharField(widget=forms.TextInput(), required=False)
    hw_repl_vend_fk = ModelChoiceField(queryset=Vendor.objects.all().order_by('vend_name'), initial=0, required=False)
    hw_cust_fk = ModelChoiceField(queryset=Customer.objects.all().order_by('cust_name'), initial=0, required=False)
    hw_portsts_fk = ModelChoiceField(queryset=PortfolioStatus.objects.all(), initial=0, required=False)
    hw_hwcat_fk = ModelChoiceField(queryset=HardwareCategory.objects.all().order_by('hwcat_name'), initial=0, required=False)
    hw_hwsts_fk = ModelChoiceField(queryset=HardwareStatus.objects.all(), initial=0, required=False)
    hw_int_code = forms.CharField(widget=forms.TextInput(), required=False)
    hw_ext_code = forms.CharField(widget=forms.TextInput(), required=False)
    hw_eol_date = forms.DateField(widget=DatePicker(), required=False) # End of Life
    hw_eow_date = forms.DateField(widget=DatePicker(), required=False) # End of Warranty
    hw_ems_date = forms.DateField(widget=DatePicker(), required=False) # End of Mainstream Support
    hw_ees1_date = forms.DateField(widget=DatePicker(), required=False) # End of Extended Support - Period One
    hw_ees2_date = forms.DateField(widget=DatePicker(), required=False) # End of Extended Support - Period Two
    hw_ees3_date = forms.DateField(widget=DatePicker(), required=False) # End of Extended Support - Period Three
    hw_see_txt = forms.CharField(widget=forms.TextInput(), required=False) # Support End Estimated
    hw_plp_txt = forms.CharField(widget=forms.TextInput(), required=False) # Product Lifecycle Policy
    hw_upd_date = forms.DateField(widget=DatePicker(), required=False)
    hw_int_reference = forms.CharField(widget=forms.TextInput(), required=False)

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
            "hw_see_txt",
            "hw_plp_txt",
            "hw_upd_date",
            "hw_int_reference",
        ]
        labels = {
            "hw_description" : "Hardware Description",
            "hw_vend_fk" : "Vendor",        
            "hw_repl_desc" : "Replacement Hardware Description",
            "hw_repl_vend_fk" : "Replacement Vendor",
            "hw_cust_fk" : "Customer",
            "hw_portsts_fk" : "Portfolio Status",
            "hw_hwcat_fk" : "Hardware Category",
            "hw_hwsts_fk" : "Hardware Status",
            "hw_int_code" : "Internal Part Code",
            "hw_ext_code" : "External Part Code",
            "hw_eol_date" : "End of Life",
            "hw_eow_date" : "End of Warranty",
            "hw_ems_date" : "End of Mainstream Support",
            "hw_ees1_date" : "End of Extended Support - Period 1",
            "hw_ees2_date" : "End of Extended Support - Period 2",
            "hw_ees3_date" : "End of Extended Support - Period 3",
            "hw_see_txt" : "Support End Estimated",
            "hw_plp_txt" : "Product Lifecycle Policy",
            "hw_upd_date" : "Information Updated",
            "hw_int_reference" : "Internal Process Reference",            
        }