from django import views
from django.shortcuts import render


# Create your views here.
def frontpage(request):
    return render(request, 'app/frontpage.html')

def privacy(request):
    return render(request, 'app/privacy.html')

def terms(request):
    return render(request, 'app/terms.html')

def plans(request):
    return render(request, 'app/plans.html')

def about(request):
    return render(request, 'app/about.html')