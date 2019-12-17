from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import permission_required
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
from .models import Software, SoftwareContact, SoftwareNote, SWPortfolioStatus, SoftwareVendor, SWVendorContact, SWVendorNote, SoftwareMatrix
from apps.lists.models import ProductType,SoftwareCategory,SoftwareStatus
from apps.customers.models import Customer
from apps.vendors.models import Vendor
from .forms import SoftwareModelForm, SoftwareVendorModelForm, SoftwareMatrixModelForm, SoftwareMatrixForm


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
    
    
    def get_context_data(self, **kwargs):
        context = super(SoftwareDetailView, self).get_context_data(**kwargs)
        self.request.session['swprd_id'] = self.object.sw_id
        context.update({
        'sw_customers' : SoftwareMatrix.objects.filter(swmtx_sw_fk=self.kwargs['pk']),
        'sw_contacts' : SoftwareContact.objects.filter(swcontact_sw_fk=self.kwargs['pk']),
        'sw_notes' : SoftwareNote.objects.filter(swnote_sw_fk=self.kwargs['pk']),
        })        
        return context

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
    swvendqs = SoftwareVendor.objects.all().order_by('swvend_name')
    swvendorDesc_query = request.GET.get('swvendorDesc')
    
    if swvendorDesc_query != '' and swvendorDesc_query is not None:
        swvendqs = swvendqs.filter(swvend_name__icontains=swvendorDesc_query).order_by('swvend_name')
            
    paginator = Paginator(swvendqs, 25)
    
    page = request.GET.get('page')
    
    swvendqs = paginator.get_page(page)
    
    context = {
        'queryset': swvendqs
    }
    
    return render(request,"software/softwarevendor_home.html",context)


class SWVendorDetailView(LoginRequiredMixin, DetailView):
    model = SoftwareVendor
    
    
    def get_context_data(self, **kwargs):
        context = super(SWVendorDetailView, self).get_context_data(**kwargs)
        self.request.session['swvend_id'] = self.object.swvend_id
        context.update({
        'swvend_products' : Software.objects.filter(sw_vend_fk=self.kwargs['pk']),
        'swvend_contacts' : SWVendorContact.objects.filter(swvendcontact_vend_fk=self.kwargs['pk']),
        'swvend_notes' : SWVendorNote.objects.filter(swvendnote_vend_fk=self.kwargs['pk']),
        })        
        return context
    

class SWVendorCreateView(LoginRequiredMixin, CreateView):
    model = SoftwareVendor
    form_class = SoftwareVendorModelForm
    
    def form_valid(self, form):
        form.instance.swvend_createdby = self.request.user
        form.instance.swvend_modifiedby = self.request.user
        return super().form_valid(form)
    
        
class SWVendorUpdateView(LoginRequiredMixin, UpdateView):
    model = SoftwareVendor
    form_class = SoftwareVendorModelForm
    
    def form_valid(self, form):
        form.instance.swvend_modifiedby = self.request.user
        return super().form_valid(form)

    
class SWVendorDeleteView(LoginRequiredMixin, DeleteView):
    model = SoftwareVendor
    success_url = '/'
    
    
class SWMatrixDetailView(LoginRequiredMixin, DetailView):
    model = SoftwareMatrix
    request.session['swmtx_id'] = object.swmtx_id

    
@permission_required('admin.can_add_log_entry') 
def SWMatrixCreateView(request):
    initial_data = {
        'swmtx_sw_fk': request.session['swprd_id'],
        'swmtx_createdby': request.user,
        'swmtx_modifiedby': request.user
    }
    
    swmtx_create_form = SoftwareMatrixForm(request.POST or None, initial=initial_data)
    
    if swmtx_create_form.is_valid():
        swmtx_create_form.save()
        return redirect('software-detail', pk=request.session['swprd_id'])
         
    context = {
        'form': swmtx_create_form
    }
    
    return render(request, "software/softwarematrix_form.html", context)


class SWMatrixCreateModelView(LoginRequiredMixin, CreateView):
    model = SoftwareMatrix
    form_class = SoftwareMatrixModelForm
    
    
    def form_valid(self, form):
        form.instance.swvend_createdby = self.request.user
        form.instance.swvend_modifiedby = self.request.user
        return super().form_valid(form)
    
        
class SWMatrixUpdateView(LoginRequiredMixin, UpdateView):
    model = SoftwareMatrix
    form_class = SoftwareMatrixModelForm
    
    def form_valid(self, form):
        form.instance.swvend_modifiedby = self.request.user
        return super().form_valid(form)

    
class SWMatrixDeleteView(LoginRequiredMixin, DeleteView):
    model = SoftwareMatrix
    
    def get_success_url (self):
        return reverse_lazy('software-detail', kwargs={'pk': self.request.session['swprd_id']})