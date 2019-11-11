import django_filters as filters
from django.utils.translation import gettext_lazy as _
from .models import Software

class SoftwareFilter(filters.FilterSet):

    class Meta:
        model = Software
        fields = {
            'sw_description': ['icontains']
                }  

  