"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
from .views import (
    CustomerFilterView,
    CustomerDetailView,
    CustomerCreateView,
    CustomerUpdateView,
    CustomerDeleteView,
    CustProjectCreateView,
)

urlpatterns = [
    path('customers/', CustomerFilterView, name='cust-home'),
    path('customer/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),
    path('customer/new/', CustomerCreateView.as_view(), name='customer-create'),
    path('customer/<int:pk>/update/', CustomerUpdateView.as_view(), name='customer-update'),
    path('customer/<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer-delete'),
    path('customer/new/project/', CustProjectCreateView.as_view(), name='cust-project-create'),
]