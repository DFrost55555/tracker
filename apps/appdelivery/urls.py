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
    AppDeliveryView,
#     SoftwareDetailView,
#     SoftwareCreateView,
#     SoftwareUpdateView,
#     SoftwareDeleteView,
)
urlpatterns = [
    path('delivery/', AppDeliveryView, name='delivery-home'),
    # path('software/<int:pk>/', SoftwareDetailView.as_view(), name='software-detail'),
    # path('software/new/', SoftwareCreateView.as_view(), name='software-create'),
    # path('software/<int:pk>/update/', SoftwareUpdateView.as_view(), name='software-update'),
    # path('software/<int:pk>/delete/', SoftwareDeleteView.as_view(), name='software-delete'),
]