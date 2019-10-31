from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User, Group
from .forms import CustProjectModelForm
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
from apps.statustype.models import StatusType
from apps.chgcodetype.models import ChgCodeType
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


class CustProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = CustProjectModelForm
    template_name = 'customers/customer_project_form.html'
       
    def form_valid(self, form):
        form.instance.project_customer_fk = self.request.session['cust_id']
        #form.instance.project_chargecodetype_fk = ChgCodeType.objects.get(pk=cleaned_data['project_chargecodetype_fk'])
        #form.instance.project_statustype_fk = StatusType.objects.get(pk=cleaned_data['project_statustype_fk'])
        form.instance.project_createdby = self.request.user
        form.instance.project_modifiedby = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        url = 'customer/<int:' + self.request.session['cust_id'] + '>/'
        return url
