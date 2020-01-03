from django.shortcuts import render

def rep_plm_home(request):
    return render(request, 'reportsplm/rep_plm_home.html', {'title': 'PLM Reports Home'})
