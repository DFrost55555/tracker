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
from .forms import PurOrderModelForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import PurchaseOrder
#from apps.customers.models import Customer
#from apps.statustype.models import StatusType
#from apps.chgcodetype.models import ChgCodeType
#from apps.lists.models import Location, ProjectStatus, ResourceStatus, ChargeCodeType, ChargeUnitType
#from .filters import ProjectFilter

def PurOrdersFilterView(request):
    qs = PurchaseOrder.objects.all().order_by('po_reference')
    poReference_query = request.GET.get('poReference')
    
    if poReference_query != '' and poReference_query is not None:
        qs = qs.filter(po_reference__icontains=poReference_query).order_by('po_reference')
            
    paginator = Paginator(qs, 10)
    
    page = request.GET.get('page')
    
    qs = paginator.get_page(page)
    
    context = {
        'queryset': qs
    }
    
    return render(request,"purorders/purchaseorder_home.html",context)


class PurOrdersDetailView(LoginRequiredMixin, DetailView):
    model = PurchaseOrder
    

class PurOrdersCreateView(LoginRequiredMixin, CreateView):
    model = PurchaseOrder
    form_class = PurOrderModelForm
    
    def form_valid(self, form):
        form.instance.po_createdby = self.request.user
        form.instance.po_modifiedby = self.request.user
        return super().form_valid(form)
    
        
class PurOrdersUpdateView(LoginRequiredMixin, UpdateView):
    model = PurchaseOrder
    form_class = PurOrderModelForm
    
    def form_valid(self, form):
        form.instance.po_modifiedby = self.request.user
        return super().form_valid(form)

    
class PurOrdersDeleteView(LoginRequiredMixin, DeleteView):
    model = PurchaseOrder
    success_url = '/'
