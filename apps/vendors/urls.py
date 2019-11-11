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
    VendorFilterView,
    VendorDetailView,
    VendorCreateView,
    VendorUpdateView,
    VendorDeleteView,
)
urlpatterns = [
    path('vendor/', VendorFilterView, name='vendor-home'),
    path('vendor/<int:pk>/', VendorDetailView.as_view(), name='vendor-detail'),
    path('vendor/new/', VendorCreateView.as_view(), name='vendor-create'),
    path('vendor/<int:pk>/update/', VendorUpdateView.as_view(), name='vendor-update'),
    path('vendor/<int:pk>/delete/', VendorDeleteView.as_view(), name='vendor-delete'),
]