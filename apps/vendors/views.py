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
from .models import Vendor, VendorContact, VendorNote
from apps.customers.models import Customer
from apps.vendors.models import Vendor


# Create your views here.

def VendorFilterView(request):
    vendqs = Vendor.objects.all().order_by('vend_description')
    vendorDesc_query = request.GET.get('vendorDesc')
    
    if vendorDesc_query != '' and vendorDesc_query is not None:
        vendqs = vendqs.filter(vend_name__icontains=vendorDesc_query).order_by('vend_name')
            
    paginator = Paginator(vendqs, 10)
    
    page = request.GET.get('page')
    
    vendqs = paginator.get_page(page)
    
    context = {
        'queryset': vendqs
    }
    
    return render(request,"vendor/vendor_home.html",context)


class VendorDetailView(LoginRequiredMixin, DetailView):
    model = Vendor
    

class VendorCreateView(LoginRequiredMixin, CreateView):
    model = Vendor
    fields = ['vend_name']
    
    def form_valid(self, form):
        form.instance.vend_createdby = self.request.user
        form.instance.vend_modifiedby = self.request.user
        return super().form_valid(form)
    
        
class VendorUpdateView(LoginRequiredMixin, UpdateView):
    model = Vendor
    fields = ['vend_name']
    
    def form_valid(self, form):
        form.instance.vend_modifiedby = self.request.user
        return super().form_valid(form)

    
class VendorDeleteView(LoginRequiredMixin, DeleteView):
    model = Vendor
    success_url = '/'