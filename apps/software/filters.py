import django_filters
from django_filters import DateFilter, CharFilter
from django.utils.translation import gettext_lazy as _
from .models import Software,SoftwareVendor,SoftwareMatrix
from apps.lists.models import ProductType,SoftwareCategory,SoftwareStatus
from apps.vendors.models import Vendor

class SoftwareFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='sw_eol_date', lookup_expr='gte', label='EOS Greater Than')
    end_date = DateFilter(field_name='sw_eol_date', lookup_expr='lte',  label='EOS Less Than')
    sw_description = CharFilter(field_name='sw_description', lookup_expr='icontains', label='Description')
    sw_version = CharFilter(field_name='sw_version', lookup_expr='icontains', label='Version')
    class Meta:
        model = Software
        fields = {
            'sw_vend_fk',
            'sw_description',
            'sw_version'
                }  

  