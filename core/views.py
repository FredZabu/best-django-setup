from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import customUserCreationForm

def home(request):
    return render(request, 'home.html')

class SignupView(CreateView):
    form_class = customUserCreationForm
    success_url = '/accounts/login'
    template_name = 'registration/signup.html'