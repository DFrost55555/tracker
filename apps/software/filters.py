import django_filters
from django_filters import DateFilter, CharFilter
from django.utils.translation import gettext_lazy as _
from .models import Software,SoftwareVendor,SoftwareMatrix
from apps.lists.models import ProductType,SoftwareCategory,SoftwareStatus
from apps.customers.models import Customer
from apps.vendors.models import Vendor

class SoftwareFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='sw_eol_date', lookup_expr='gte')
    end_date = DateFilter(field_name='sw_eol_date', lookup_expr='lte')
    sw_description = CharFilter(field_name='sw_description', lookup_expr='icontains')
    sw_version = CharFilter(field_name='sw_version', lookup_expr='icontains')
    class Meta:
        model = Software
        fields = {
            'sw_description',
            'sw_version',
            'sw_vend_fk',
            'sw_swcat_fk',
            'sw_swsts_fk'
                }  

  