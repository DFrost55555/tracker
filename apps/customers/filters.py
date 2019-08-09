import django_filters as filters
from django.utils.translation import gettext_lazy as _
from .models import Customer

class CustomerFilter(filters.FilterSet):

    class Meta:
        model = Customer
        fields = {
            'cust_name': ['icontains']
                }  

  