from django.shortcuts import render

def prj_home(request):
    return render(request, 'projects/prj_home.html', {'title': 'Projects Home'})
