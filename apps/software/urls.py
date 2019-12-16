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
    SoftwareFilterView,
    SoftwareDetailView,
    SoftwareCreateView,
    SoftwareUpdateView,
    SoftwareDeleteView,
    SWVendorFilterView,
    SWVendorDetailView,
    SWVendorCreateView,
    SWVendorUpdateView,
    SWVendorDeleteView,
    SWMatrixDetailView,
    SWMatrixCreateView,
    SWMatrixUpdateView,
    SWMatrixDeleteView,
)
urlpatterns = [
    path('software/', SoftwareFilterView, name='software-home'),
    path('software/<int:pk>/', SoftwareDetailView.as_view(), name='software-detail'),
    path('software/new/', SoftwareCreateView.as_view(), name='software-create'),
    path('software/<int:pk>/update/', SoftwareUpdateView.as_view(), name='software-update'),
    path('software/<int:pk>/delete/', SoftwareDeleteView.as_view(), name='software-delete'),
    path('software/vendor/', SWVendorFilterView, name='swvend-home'),
    path('software/vendor/<int:pk>/', SWVendorDetailView.as_view(), name='swvend-detail'),
    path('software/vendor/new/', SWVendorCreateView.as_view(), name='swvend-create'),
    path('software/vendor/<int:pk>/update/', SWVendorUpdateView.as_view(), name='swvend-update'),
    path('software/vendor/<int:pk>/delete/', SWVendorDeleteView.as_view(), name='swvend-delete'),
    path('software/matrix/<int:pk>/', SWMatrixDetailView.as_view(), name='swmtx-detail'),
    path('software/matrix/new/', SWMatrixCreateView.as_view(), name='swmtx-create'),
    path('software/matrix/<int:pk>/update/', SWMatrixUpdateView.as_view(), name='swmtx-update'),
    path('software/matrix/<int:pk>/delete/', SWMatrixDeleteView.as_view(), name='swmtx-delete'),
]