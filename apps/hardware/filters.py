import django_filters as filters
from django.utils.translation import gettext_lazy as _
from .models import Hardware

class HardwareFilter(filters.FilterSet):

    class Meta:
        model = Hardware
        fields = {
            'hw_description': ['icontains']
                }  

  