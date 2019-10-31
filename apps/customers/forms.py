from django import forms
from .models import Customer
from apps.projects.models import Project
from apps.statustype.models import StatusType
from apps.chgcodetype.models import ChgCodeType
from django.forms import ModelChoiceField, HiddenInput


