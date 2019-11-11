import django_filters as filters
from django.utils.translation import gettext_lazy as _
from .models import Vendor

class VendorFilter(filters.FilterSet):

    class Meta:
        model = Vendor
        fields = {
            'vend_name': ['icontains']
                }  