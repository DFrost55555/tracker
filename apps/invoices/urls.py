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
    InvoicesFilterView,
    InvoicesDetailView,
    InvoicesCreateView,
    InvoicesUpdateView,
    InvoicesDeleteView,
)
urlpatterns = [
    path('invoices/', InvoicesFilterView, name='invoices-home'),
    path('invoices/<int:pk>/', InvoicesDetailView.as_view(), name='invoices-detail'),
    path('invoices/new/', InvoicesCreateView.as_view(), name='invoices-create'),
    path('invoices/<int:pk>/update/', InvoicesUpdateView.as_view(), name='invoices-update'),
    path('invoices/<int:pk>/delete/', InvoicesDeleteView.as_view(), name='invoices-delete'),
]