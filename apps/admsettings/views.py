from django.shortcuts import render

def admset_home(request):
    return render(request, 'admsettings/admset_home.html', {'title': 'ADM Settings Home'})
