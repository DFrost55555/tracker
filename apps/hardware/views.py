from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Hardware, HardwareContact, HardwareNote, PortfolioStatus
from apps.lists.models import ProductType,HardwareCategory,HardwareStatus
from apps.customers.models import Customer
from apps.vendors.models import Vendor


# Create your views here.

def HardwareFilterView(request):
    hwqs = Hardware.objects.all().order_by('hw_description')
    hardwareDesc_query = request.GET.get('hardwareDesc')
    
    if hardwareDesc_query != '' and hardwareDesc_query is not None:
        hwqs = hwqs.filter(hw_description__icontains=hardwareDesc_query).order_by('hw_description')
            
    paginator = Paginator(hwqs, 10)
    
    page = request.GET.get('page')
    
    hwqs = paginator.get_page(page)
    
    context = {
        'queryset': hwqs
    }
    
    return render(request,"hardware/hardware_home.html",context)


class HardwareDetailView(LoginRequiredMixin, DetailView):
    model = Hardware
    

class HardwareCreateView(LoginRequiredMixin, CreateView):
    model = Hardware
    fields = ['project_name', 'project_customer_fk', 'project_reference', 'project_chargecode', 'project_chargecodetype_fk', 'project_statustype_fk']
    
    def form_valid(self, form):
        form.instance.hw_createdby = self.request.user
        form.instance.hw_modifiedby = self.request.user
        return super().form_valid(form)
    
        
class HardwareUpdateView(LoginRequiredMixin, UpdateView):
    model = Hardware
    fields = ['project_name', 'project_customer_fk', 'project_reference', 'project_chargecode', 'project_chargecodetype_fk', 'project_statustype_fk']
    
    def form_valid(self, form):
        form.instance.hw_modifiedby = self.request.user
        return super().form_valid(form)

    
class HardwareDeleteView(LoginRequiredMixin, DeleteView):
    model = Hardware
    success_url = '/'