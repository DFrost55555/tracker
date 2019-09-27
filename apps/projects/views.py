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
from tracker.apps.customers.models import Customer

def prj_home(request):
    return render(request, 'projects/prj_home.html', {'title': 'Projects Home'})

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['project_name', 'project_customer_fk']
    
    def form_valid(self, form):
        form.instance.project_createdby = self.request.user
        form.instance.project_modifiedby = self.request.user
        return super().form_valid(form)