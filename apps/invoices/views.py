from django.core.paginator import Paginator
from django.utils import timezone
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
from .forms import InvoiceModelForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Invoice, INVMatrix, INVStatus, INVType, INVNote
#from apps.customers.models import Customer
#from apps.statustype.models import StatusType
#from apps.chgcodetype.models import ChgCodeType
#from apps.lists.models import Location, ProjectStatus, ResourceStatus, ChargeCodeType, ChargeUnitType
#from .filters import ProjectFilter

def InvoicesFilterView(request):
    qs = Invoice.objects.all().order_by('inv_reference')
    invReference_query = request.GET.get('invReference')
    
    if invReference_query != '' and invReference_query is not None:
        qs = qs.filter(inv_reference__icontains=invReference_query).order_by('inv_reference')
            
    paginator = Paginator(qs, 10)
    
    page = request.GET.get('page')
    
    qs = paginator.get_page(page)
    
    context = {
        'queryset': qs
    }
    
    return render(request,"invoices/invoice_home.html",context)


class InvoicesDetailView(LoginRequiredMixin, DetailView):
    model = Invoice
    

class InvoicesCreateView(LoginRequiredMixin, CreateView):
    model = Invoice
    form_class = InvoiceModelForm
    
    def form_valid(self, form):
        form.instance.inv_createdby = self.request.user
        form.instance.inv_modifiedby = self.request.user
        return super().form_valid(form)
    
        
class InvoicesUpdateView(LoginRequiredMixin, UpdateView):
    model = Invoice
    fields = [
            'inv_reference',
            'inv_quantity',
            'inv_quantity_type_fk',
            'inv_cost_value',
            'inv_unit_cost',
            'inv_date',
            'inv_gr_reference',
            'inv_gr_date',
        ]
    
    def form_valid(self, form):
        form.instance.inv_modifiedby = self.request.user
        return super().form_valid(form)

    
class InvoicesDeleteView(LoginRequiredMixin, DeleteView):
    model = Invoice
    success_url = '/'