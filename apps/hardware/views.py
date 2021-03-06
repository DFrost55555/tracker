import csv, io
from itertools import chain
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.core.paginator import Paginator
from django.urls import reverse
from django.contrib.auth.decorators import permission_required
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
from .models import Hardware, HardwareContact, HardwareNote, PortfolioStatus, HardwareMatrix, PortfolioCategory
from .forms import HardwareModelForm
from apps.lists.models import ProductType,HardwareCategory,HardwareStatus
from apps.customers.models import Customer
from apps.vendors.models import Vendor


# Create your views here.

def HardwareFilterView(request):
    hwqs = Hardware.objects.all().order_by('hw_description')
    hardwareDesc_query = request.GET.get('hardwareDesc')
    
    if hardwareDesc_query != '' and hardwareDesc_query is not None:
        hwqs = hwqs.filter(hw_description__icontains=hardwareDesc_query).order_by('hw_description')
            
    paginator = Paginator(hwqs, 20)
    
    page = request.GET.get('page')
    
    hwqs = paginator.get_page(page)
    
    context = {
        'queryset': hwqs
    }
    
    return render(request,"hardware/hardware_home.html",context)


class HardwareDetailView(LoginRequiredMixin, DetailView):
    model = Hardware

    def get_context_data(self, **kwargs):
        context = super(HardwareDetailView, self).get_context_data(**kwargs)
        self.request.session['hardware_id'] = self.object.hw_id  
        context.update({
        'hw_notes' : HardwareNote.objects.filter(hwnote_hw_fk=self.kwargs['pk']),
        'hw_contacts' : HardwareContact.objects.filter(hwcontact_hw_fk=self.kwargs['pk']),
        'hw_customers' : HardwareMatrix.objects.filter(hwmtx_hw_fk=self.kwargs['pk']),
        })
        return context
    

class HardwareCreateView(LoginRequiredMixin, CreateView):
    model = Hardware
    #fields = ['hw_description','hw_vend_fk','hw_repl_desc','hw_repl_vend_fk','hw_cust_fk','hw_portsts_fk','hw_hwcat_fk','hw_hwsts_fk','hw_int_code','hw_ext_code','hw_eol_date','hw_eow_date','hw_ems_date','hw_ees1_date','hw_ees2_date','hw_ees3_date','hw_see_txt','hw_plp_txt','hw_upd_date','hw_int_reference']
    form_class = HardwareModelForm
    
    def form_valid(self, form):
        form.instance.hw_createdby = self.request.user
        form.instance.hw_modifiedby = self.request.user
        return super().form_valid(form)
    
        
class HardwareUpdateView(LoginRequiredMixin, UpdateView):
    model = Hardware
    #fields = ['hw_description','hw_vend_fk','hw_repl_desc','hw_repl_vend_fk','hw_cust_fk','hw_portsts_fk','hw_hwcat_fk','hw_hwsts_fk','hw_int_code','hw_ext_code','hw_eol_date','hw_eow_date','hw_ems_date','hw_ees1_date','hw_ees2_date','hw_ees3_date','hw_see_txt','hw_plp_txt','hw_upd_date','hw_int_reference']
    form_class = HardwareModelForm
    
    def form_valid(self, form):
        form.instance.hw_modifiedby = self.request.user
        return super().form_valid(form)

    
class HardwareDeleteView(LoginRequiredMixin, DeleteView):
    model = Hardware
    success_url = '/'
    

@permission_required('admin.can_add_log_entry')    
def HardwareCSVExportView(request):
    
    hw_items = Hardware.objects.all()
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename="hardware_list.csv"'
    
    writer = csv.writer(response, delimiter=',')
    writer.writerow(['hw_description', 'hw_vend_fk', 'hw_repl_desc','hw_repl_vend_fk','hw_cust_fk', 'hw_portsts_fk', 'hw_hwcat_fk', 'hw_hwsts_fk', 'hw_int_code', 'hw_ext_code', 'hw_eol_date', 'hw_eow_date', 'hw_ems_date', 'hw_ees1_date', 'hw_ees2_date', 'hw_ees3_date', 'hw_see_yn_fk', 'hw_plp_txt', 'hw_upd_date', 'hw_int_reference'])
    
    for obj in hw_items:
        writer.writerow([obj.hw_description, obj.hw_vend_fk, obj.hw_repl_desc, obj.hw_repl_vend_fk, obj.hw_cust_fk, obj.hw_portsts_fk, obj.hw_hwcat_fk, obj.hw_hwsts_fk, obj.hw_int_code, obj.hw_ext_code, obj.hw_eol_date, obj.hw_eow_date, obj.hw_ems_date, obj.hw_ees1_date, obj.hw_ees2_date, obj.hw_ees3_date, obj.hw_see_yn_fk, obj.hw_plp_txt, obj.hw_upd_date, obj.hw_int_reference])
        
    return response