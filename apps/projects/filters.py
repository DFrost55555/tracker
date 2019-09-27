import django_filters as filters
from django.utils.translation import gettext_lazy as _
from .models import Project

class ProjectFilter(filters.FilterSet):

    class Meta:
        model = Project
        fields = {
            'project_name': ['icontains']
                }  

  