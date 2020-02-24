from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from hdps import forms
from .models import Profile
# Create your views here.
class SignUp(CreateView):
    form_class = forms.SignUpForm
    success_url = reverse_lazy('hdps:login')
    template_name = 'signup.html'

class ProfileForm(CreateView):
    form_class = forms.ProfileModelForm
    success_url = reverse_lazy('home')
    template_name = 'profile_form.html'

def home(request):
    return render(request,'home.html')
