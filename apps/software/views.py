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
from .models import Software, SoftwareContact, SoftwareNote, SWPortfolioStatus
from apps.lists.models import ProductType,SoftwareCategory,SoftwareStatus
from apps.customers.models import Customer
from apps.vendors.models import Vendor


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
    fields = ['sw_description','sw_vend_fk','sw_repl_desc','sw_repl_vend_fk','sw_cust_fk','sw_portsts_fk','sw_swcat_fk','sw_swsts_fk','sw_int_code','sw_ext_code','sw_eol_date','sw_eow_date','sw_ems_date','sw_ees1_date','sw_ees2_date','sw_ees3_date','sw_see_txt','sw_plp_txt','sw_upd_date','sw_int_reference']
    
    def form_valid(self, form):
        form.instance.sw_createdby = self.request.user
        form.instance.sw_modifiedby = self.request.user
        return super().form_valid(form)
    
        
class SoftwareUpdateView(LoginRequiredMixin, UpdateView):
    model = Software
    fields = ['sw_description','sw_vend_fk','sw_repl_desc','sw_repl_vend_fk','sw_cust_fk','sw_portsts_fk','sw_swcat_fk','sw_swsts_fk','sw_int_code','sw_ext_code','sw_eol_date','sw_eow_date','sw_ems_date','sw_ees1_date','sw_ees2_date','sw_ees3_date','sw_see_txt','sw_plp_txt','sw_upd_date','sw_int_reference']
    
    def form_valid(self, form):
        form.instance.sw_modifiedby = self.request.user
        return super().form_valid(form)

    
class SoftwareDeleteView(LoginRequiredMixin, DeleteView):
    model = Software
    success_url = '/'