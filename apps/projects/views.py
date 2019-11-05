from django.core.paginator import Paginator
from django.utils import timezone
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
from .forms import ProjectModelForm, CustProjectModelForm
from django.shortcuts import render, get_object_or_404
from .models import Project
from apps.customers.models import Customer
from apps.statustype.models import StatusType
from apps.chgcodetype.models import ChgCodeType
from apps.lists.models import Location, ProjectStatus, ResourceStatus, ChargeCodeType, ChargeUnitType
from .filters import ProjectFilter


def ProjectFilterView(request):
    qs = Project.objects.all().order_by('project_name')
    projectName_query = request.GET.get('projectName')
    
    if projectName_query != '' and projectName_query is not None:
        qs = qs.filter(cust_name__icontains=projectName_query).order_by('project_name')
            
    paginator = Paginator(qs, 10)
    
    page = request.GET.get('page')
    
    qs = paginator.get_page(page)
    
    context = {
        'queryset': qs
    }
    
    return render(request,"projects/project_home.html",context)


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['project_name', 'project_customer_fk', 'project_reference', 'project_chargecode', 'project_chargecodetype_fk', 'project_statustype_fk']
    
    def form_valid(self, form):
        form.instance.project_createdby = self.request.user
        form.instance.project_modifiedby = self.request.user
        return super().form_valid(form)
    
        
class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    fields = ['project_name', 'project_customer_fk', 'project_reference', 'project_chargecode', 'project_chargecodetype_fk', 'project_statustype_fk']
    
    def form_valid(self, form):
        form.instance.project_modifiedby = self.request.user
        return super().form_valid(form)

    
class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    success_url = '/'


class CustProjectCreateView(LoginRequiredMixin, TemplateView):
    model = Project
    form_class = CustProjectModelForm
    template_name = 'projects/customer_project_form.html'
       
    def form_valid(self, form):
        form.instance.project_customer_fk = Customer.objects.get(id=self.request.session['cust_id'])
        form.instance.project_createdby = self.request.user
        form.instance.project_modifiedby = self.request.user
        return super().form_valid(form)
    #
    # def get_initial(self, *args, **kwargs):
    #     initial = super(CustProjectCreateView, self).get_initial(**kwargs)
    #     initial['project_customer_fk'] = self.request.session['cust_id']
    #     return initial
    
    def get_success_url(self):
        url = '../customer/' + self.request.session['cust_id'] + '/'
        return url