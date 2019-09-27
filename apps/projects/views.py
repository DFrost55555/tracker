from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User, Group
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .forms import ProjectModelForm
from django.shortcuts import render, get_object_or_404
from .models import Project
from apps.customers.models import Customer
from .filters import CustomerFilter


def ProjectFilterView(request):
    qs = Project.objects.all().order_by('project_name')
    projectName_query = request.GET.get('projectName')
    
    if projectName_query != '' and projectName_query is not None:
        qs = qs.filter(cust_name__icontains=projectName_query).order_by('project_name')
            
    paginator = Paginator(qs, 10)
    
    page = request.GET.get('page')
    
    qs = paginator.get_page(page)
    
    context = {
        'queryset': qs
    }
    
    return render(request,"projects/project_home.html",context)


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['project_name', 'project_customer_fk']
    
    def form_valid(self, form):
        form.instance.project_createdby = self.request.user
        form.instance.project_modifiedby = self.request.user
        return super().form_valid(form)