from django import forms
#from django.contrib.admin.widgets import AdminDateWidget
#from bootstrap_datepicker_plus import DatePickerInput
from django.forms import ModelChoiceField
#from bootstrap_datepicker.widgets import DatePicker
from .models import Software, SoftwareContact, SoftwareNote, SWPortfolioStatus, SWPortfolioCategory, SoftwareVendor, SWVendorContact, SWVendorNote
from apps.lists.models import ProductType, SoftwareCategory, SoftwareStatus, SoftwareClassification, YesNo, TrueFalse, SoftwareFrequency, VendorFrequency
from apps.customers.models import Customer
from apps.vendors.models import Vendor

class DatePicker(forms.DateInput):
    input_type = 'date'


class SoftwareModelForm(forms.ModelForm):
    sw_version = forms.CharField(label='Software Version', widget=forms.TextInput(), required=True)
    sw_description = forms.CharField(label='Software Description', widget=forms.TextInput(), required=True)
    sw_vend_fk = ModelChoiceField(label='Vendor', queryset=SoftwareVendor.objects.all().order_by('swvend_name'), initial=0, required=True)
    sw_progver_code = forms.CharField(label='Version In Progress', widget=forms.TextInput(), required=False)
    sw_latestver_code = forms.CharField(label='Latest Available Version', widget=forms.TextInput(), required=False)
    sw_cust_notified = forms.DateField(label='Customer Notified', widget=DatePicker(), required=False)
    sw_repl_ver = forms.CharField(label='Replacement Software Version', widget=forms.TextInput(), required=False)
    sw_repl_desc = forms.CharField(label='Replacement Software Description', widget=forms.TextInput(), required=False)
    sw_repl_vend_fk = ModelChoiceField(label='Replacement Vendor', queryset=SoftwareVendor.objects.all().order_by('swvend_name'), initial=0, required=False)
    sw_cust_fk = ModelChoiceField(label='Customer', queryset=Customer.objects.all().order_by('cust_name'), initial=0, required=False)
    sw_cust_ref = forms.CharField(label='Customer Reference', widget=forms.TextInput(), required=False)
    sw_portsts_fk = ModelChoiceField(label='Portfolio Status', queryset=SWPortfolioStatus.objects.all(), initial=0, required=False)
    sw_portcat_fk = ModelChoiceField(label='Portfolio Category', queryset=SWPortfolioCategory.objects.all(), initial=0, required=False)
    sw_swclass_fk = ModelChoiceField(label='Software Classification', queryset=SoftwareClassification.objects.all().order_by('swclass_name'), initial=0, required=False)
    sw_swcat_fk = ModelChoiceField(label='Software Category', queryset=SoftwareCategory.objects.all().order_by('swcat_name'), initial=0, required=False)
    sw_swsts_fk = ModelChoiceField(label='Software Status', queryset=SoftwareStatus.objects.all(), initial=0, required=False)
    sw_swfreq_fk = ModelChoiceField(label='Agreed Release Frequency', queryset=SoftwareFrequency.objects.all(), initial=0, required=False)
    sw_vendfreq_fk = ModelChoiceField(label='Vendor Release Frequency', queryset=VendorFrequency.objects.all(), initial=0, required=False)
    sw_int_code = forms.CharField(label='Internal Part Code', widget=forms.TextInput(), required=False)
    sw_ext_code = forms.CharField(label='External Part Code', widget=forms.TextInput(), required=False)
    sw_eol_date = forms.DateField(label='End of Life', widget=DatePicker(), required=False) # End of Life
    sw_eow_date = forms.DateField(label='End of Warranty', widget=DatePicker(), required=False) # End of Warranty
    sw_ems_date = forms.DateField(label='End of Mainstream Support', widget=DatePicker(), required=False) # End of Mainstream Support
    sw_ees1_date = forms.DateField(label='End of Extended Support - Period 1', widget=DatePicker(), required=False) # End of Extended Support - Period One
    sw_ees2_date = forms.DateField(label='End of Extended Support - Period 2', widget=DatePicker(), required=False) # End of Extended Support - Period Two
    sw_ees3_date = forms.DateField(label='End of Extended Support - Period 3', widget=DatePicker(), required=False) # End of Extended Support - Period Three
    sw_see_yn_fk = forms.ModelChoiceField(label='Is SEE', queryset=YesNo.objects.all().order_by('yesno_id'), initial=2, required=False) # Support End Estimated
    sw_plp_txt = forms.CharField(label='Product Lifecycle Policy', widget=forms.TextInput(), required=False) # Product Lifecycle Policy
    sw_upd_date = forms.DateField(label='Information Updated', widget=DatePicker(), required=False)
    sw_int_reference = forms.CharField(label='Internal Process Reference', widget=forms.TextInput(), required=False)

    class Meta:
        model = Software
        fields = [
            "sw_version",
            "sw_description",
            "sw_vend_fk",
            "sw_progver_code",
            "sw_latestver_code",
            "sw_cust_notified",
            "sw_repl_ver",
            "sw_repl_desc",
            "sw_repl_vend_fk",
            "sw_cust_fk",
            "sw_portsts_fk",
            "sw_portcat_fk",
            "sw_swclass_fk",
            "sw_swcat_fk",
            "sw_swsts_fk",
            "sw_swfreq_fk",
            "sw_vendfreq_fk",
            "sw_int_code",
            "sw_ext_code",
            "sw_eol_date",
            "sw_eow_date",
            "sw_ems_date",
            "sw_ees1_date",
            "sw_ees2_date",
            "sw_ees3_date",
            "sw_see_yn_fk",
            "sw_plp_txt",
            "sw_upd_date",
            "sw_int_reference",
        ]
        
        
class SoftwareVendorModelForm(forms.ModelForm):
    swvend_name = forms.CharField(label='Software Vendor', widget=forms.TextInput(), required=True)
    
    class Meta:
        model = SoftwareVendor
        fields = [
            "swvend_name",
        ]
