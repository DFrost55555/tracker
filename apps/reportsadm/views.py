from django.shortcuts import render

def rep_adm_home(request):
    return render(request, 'reportsadm/rep_adm_home.html', {'title': 'ADM Reports Home'})
