from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def cmp_home(request):
    return render(request, 'components/cmp_home.html', {'title': 'Components Home'})
