from django.shortcuts import render

def rep_home(request):
    return render(request, 'reports/rep_home.html', {'title': 'Reports Home'})
