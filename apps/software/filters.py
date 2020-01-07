import django_filters
from django import forms
from django_filters import DateFilter, CharFilter
from django.utils.translation import gettext_lazy as _
from django.forms.widgets import TextInput, DateInput, NumberInput
from .models import Software,SoftwareVendor,SoftwareMatrix
from apps.lists.models import ProductType,SoftwareCategory,SoftwareStatus

class DatePicker(forms.DateInput):
    input_type = 'date'

class SoftwareFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='sw_eol_date', lookup_expr='gte', label='EOS After')
    end_date = DateFilter(field_name='sw_eol_date', lookup_expr='lte',  label='EOS Before')
    sw_description = CharFilter(field_name='sw_description', lookup_expr='icontains', label='Product', widget=TextInput(attrs={'placeholder': 'Product name contains...'}))
    sw_version = CharFilter(field_name='sw_version', lookup_expr='icontains', label='Version', widget=TextInput(attrs={'placeholder': 'Version contains...'}))
    class Meta:
        model = Software
        fields = {
            'sw_vend_fk',
            'sw_description',
            'sw_version',
            'sw_swcat_fk',
            'sw_swsts_fk'
            }  

  