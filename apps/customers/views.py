from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User, Group
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Customer, CustomerNote, CustomerContact
from apps.projects.models import Project
from apps.hardware.models import Hardware, HardwareContact, HardwareNote, PortfolioStatus, HardwareMatrix, PortfolioCategory
from apps.software.models import Software, SoftwareContact, SoftwareNote, SWPortfolioStatus, SWPortfolioCategory, SoftwareVendor, SWVendorContact, SWVendorNote, SoftwareMatrix
from apps.lists.models import ProductType,HardwareCategory, HardwareStatus, SoftwareCategory, SoftwareStatus, SoftwareClassification, YesNo, TrueFalse, SoftwareFrequency, VendorFrequency
from .filters import CustomerFilter

def CustomerFilterView(request):
    qs = Customer.objects.all().order_by('cust_name')
    customerName_query = request.GET.get('customerName')
    
    if customerName_query != '' and customerName_query is not None:
        qs = qs.filter(cust_name__icontains=customerName_query).order_by('cust_name')
            
    paginator = Paginator(qs, 15)
    
    page = request.GET.get('page')
    
    qs = paginator.get_page(page)
    
    context = {
        'customerqs': qs
    }
    
    return render(request,"customers/cust_home.html",context)

class CustomerDetailView(LoginRequiredMixin, DetailView):
    model = Customer
    
    
    def get_context_data(self, **kwargs):
        context = super(CustomerDetailView, self).get_context_data(**kwargs)
        self.request.session['cust_id'] = self.object.id
        context.update({
        'cust_projects' : Project.objects.filter(project_customer_fk=self.kwargs['pk']),
        'cust_notes' : CustomerNote.objects.filter(custnote_customer_fk=self.kwargs['pk']),
        'cust_contacts' : CustomerContact.objects.filter(custcontact_customer_fk=self.kwargs['pk']),
        })
        return context
        
            
class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    fields = ['cust_name']
    
    def form_valid(self, form):
        form.instance.cust_createdby = self.request.user
        form.instance.cust_modifiedby = self.request.user
        return super().form_valid(form)
    
    #def get_success_url(self):
        #return reverse('cust-home')
    
class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    model = Customer
    fields = ['cust_name']
    
    def form_valid(self, form):
        form.instance.cust_modifiedby = self.request.user
        return super().form_valid(form)
    
class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    model = Customer
    success_url = '/'


def PLMCustomerFilterView(request):
    qs = Customer.objects.all().order_by('cust_name')
    plmcustomerName_query = request.GET.get('plmcustomerName')
    
    if plmcustomerName_query != '' and plmcustomerName_query is not None:
        qs = qs.filter(cust_name__icontains=plmcustomerName_query).order_by('cust_name')
            
    paginator = Paginator(qs, 15)
    
    page = request.GET.get('page')
    
    qs = paginator.get_page(page)
    
    context = {
        'plmcustomerqs': qs
    }
    
    return render(request,"customers/plm_cust_home.html",context)

class PLMCustomerDetailView(LoginRequiredMixin, DetailView):
    template_name = 'customers/plm_customer_detail.html'
    model = Customer
    
    
    def get_context_data(self, **kwargs):
        context = super(PLMCustomerDetailView, self).get_context_data(**kwargs)
        self.request.session['cust_id'] = self.object.id
        context.update({
        'cust_hardware' : HardwareMatrix.objects.filter(hwmtx_cust_fk=self.kwargs['pk']),
        'cust_software' : SoftwareMatrix.objects.filter(swmtx_cust_fk=self.kwargs['pk']),
        'cust_notes' : CustomerNote.objects.filter(custnote_customer_fk=self.kwargs['pk']),
        'cust_contacts' : CustomerContact.objects.filter(custcontact_customer_fk=self.kwargs['pk']),
        })
        return context
        
            
class PLMCustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    fields = ['cust_name']
    
    def form_valid(self, form):
        form.instance.cust_createdby = self.request.user
        form.instance.cust_modifiedby = self.request.user
        return super().form_valid(form)
    
    #def get_success_url(self):
        #return reverse('cust-home')
    
class PLMCustomerUpdateView(LoginRequiredMixin, UpdateView):
    model = Customer
    fields = ['cust_name']
    
    def form_valid(self, form):
        form.instance.cust_modifiedby = self.request.user
        return super().form_valid(form)
    
class PLMCustomerDeleteView(LoginRequiredMixin, DeleteView):
    model = Customer
    success_url = '/'