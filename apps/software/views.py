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
from .models import Software, SoftwareContact, SoftwareNote, SWPortfolioStatus, SoftwareVendor, SWVendorContact, SWVendorNote
from apps.lists.models import ProductType,SoftwareCategory,SoftwareStatus
from apps.customers.models import Customer
from apps.vendors.models import Vendor
from .forms import SoftwareModelForm


# Create your views here.

def SoftwareFilterView(request):
    swqs = Software.objects.all().order_by('sw_description')
    softwareDesc_query = request.GET.get('softwareDesc')
    
    if softwareDesc_query != '' and softwareDesc_query is not None:
        swqs = swqs.filter(sw_description__icontains=softwareDesc_query).order_by('sw_description')
            
    paginator = Paginator(swqs, 10)
    
    page = request.GET.get('page')
    
    swqs = paginator.get_page(page)
    
    context = {
        'queryset': swqs
    }
    
    return render(request,"software/software_home.html",context)


class SoftwareDetailView(LoginRequiredMixin, DetailView):
    model = Software
    

class SoftwareCreateView(LoginRequiredMixin, CreateView):
    model = Software
    form_class = SoftwareModelForm
    
    def form_valid(self, form):
        form.instance.sw_createdby = self.request.user
        form.instance.sw_modifiedby = self.request.user
        return super().form_valid(form)
    
        
class SoftwareUpdateView(LoginRequiredMixin, UpdateView):
    model = Software
    form_class = SoftwareModelForm
    
    def form_valid(self, form):
        form.instance.sw_modifiedby = self.request.user
        return super().form_valid(form)

    
class SoftwareDeleteView(LoginRequiredMixin, DeleteView):
    model = Software
    success_url = '/'
    
    
def SWVendorFilterView(request):
    swvendqs = SoftwareVendor.objects.all().order_by('swvend_description')
    swvendorDesc_query = request.GET.get('swvendorDesc')
    
    if swvendorDesc_query != '' and swvendorDesc_query is not None:
        vendqs = vendqs.filter(vend_name__icontains=swvendorDesc_query).order_by('swvend_name')
            
    paginator = Paginator(swvendqs, 10)
    
    page = request.GET.get('page')
    
    swvendqs = paginator.get_page(page)
    
    context = {
        'queryset': swvendqs
    }
    
    return render(request,"software/swvendor_home.html",context)


class SWVendorDetailView(LoginRequiredMixin, DetailView):
    model = SoftwareVendor
    

class SWVendorCreateView(LoginRequiredMixin, CreateView):
    model = SoftwareVendor
    fields = ['swvend_name']
    
    def form_valid(self, form):
        form.instance.swvend_createdby = self.request.user
        form.instance.swvend_modifiedby = self.request.user
        return super().form_valid(form)
    
        
class SWVendorUpdateView(LoginRequiredMixin, UpdateView):
    model = SoftwareVendor
    fields = ['swvend_name']
    
    def form_valid(self, form):
        form.instance.swvend_modifiedby = self.request.user
        return super().form_valid(form)

    
class SWVendorDeleteView(LoginRequiredMixin, DeleteView):
    model = SoftwareVendor
    success_url = '/'