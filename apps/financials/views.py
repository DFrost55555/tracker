from django.shortcuts import render

def fin_home(request):
    return render(request, 'financials/fin_home.html', {'title': 'Financials Home'})
