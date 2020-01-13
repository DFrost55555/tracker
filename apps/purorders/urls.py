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
    PurOrdersFilterView,
    PurOrdersDetailView,
    PurOrdersCreateView,
    PurOrdersUpdateView,
    PurOrdersDeleteView,
    #CustProjectCreateView,
)
urlpatterns = [
    path('purorders/', PurOrdersFilterView, name='purorders-home'),
    path('purorders/<int:pk>/', PurOrdersDetailView.as_view(), name='purorders-detail'),
    #path('purorders/new/', PurOrdersCreateView.as_view(), name='purorders-create'),
    #path('purorders/<int:pk>/update/', PurOrdersUpdateView.as_view(), name='purorders-update'),
    path('purorders/<int:pk>/delete/', PurOrdersDeleteView.as_view(), name='purorders-delete'),
    #path('project/new/customer/', CustProjectCreateView.as_view(), name='project-create-cust'),
]