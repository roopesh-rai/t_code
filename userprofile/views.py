from django.shortcuts import render, redirect
from .forms import CustomerRegistraionForm
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistraionForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = CustomerRegistraionForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! Registered Successfully')
            form.save()
        return render(request, 'signup.html', {'form': form})

def login(request):
    return render(request, 'login.html')

@login_required
def myaccount(request):
    return render(request, 'myaccount.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        request.user.first_name = request.POST.get('first_name', '')
        request.user.last_name = request.POST.get('last_name', '')
        request.user.email = request.POST.get('email', '')
        request.user.save()
        messages.info(request, 'The changes was saved')
        return redirect('myaccount')
    return render(request, 'edit_profile.html')