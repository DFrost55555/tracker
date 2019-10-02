import django_filters as filters
from django.utils.translation import gettext_lazy as _
from .models import Customer
from apps.projects.models import Project

class CustomerFilter(filters.FilterSet):

    class Meta:
        model = Customer
        fields = {
            'cust_name': ['icontains']
                }  


class CustomerProjectFilter(filters.FilterSet):
    
    class Meta:
        model = Project
        fields = ('project_customer_fk')