from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Customer
from .filters import CustomerFilter


def CustomerFilterView(request):
    qs = Customer.objects.all().order_by('cust_name')
    customerName_query = request.GET.get('customerName')
    
    if customerName_query != '' and customerName_query is not None:
        qs = qs.filter(cust_name__icontains=customerName_query).order_by('cust_name')
            
    paginator = Paginator(qs, 20)
    
    page = request.GET.get('page')
    
    qs = paginator.get_page(page)
    
    context = {
        'queryset': qs
    }
    
    return render(request,"customers/cust_home.html",context)

class CustomerDetailView(DetailView):
    model = Customer
    
class CustomerCreateView(CreateView):
    model = Customer
    fields = ['cust_name']



    
  
    
    
    
"""     model = Customer
    template_name = 'customers/cust_home.html'
    context_object_name = 'customers'
    ordering = ['cust_name']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = CustomerFilter(self.request.GET,queryset=self.get_queryset())
        return context """
        