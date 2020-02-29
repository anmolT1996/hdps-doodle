from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView,SingleObjectMixin
from django.views.generic.list import ListView
from hdps import forms
from .models import Profile
from .forms import ProfileModelForm,SignUpForm
# Create your views here.
class SignUp(CreateView):
    form_class = forms.SignUpForm
    success_url = reverse_lazy('hdps:login')
    template_name = 'signup.html'

class ProfileForm(LoginRequiredMixin,CreateView):
    form_class = forms.ProfileModelForm
    template_name = 'profile_form.html'

    def form_valid(self, form):
        fields = ['age','birth_date','phone_no','address','profile_pic']
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('hdps:profile-detail',kwargs={'pk':self.object.id})


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile_detail.html'

    def get_object(self):
        try:
            object = super().get_object()
        except:
            object = None
            return object
        return object



class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileModelForm
    template_name = 'profile_form.html'

    def get_object(self):
        id_ = self.request.user.id
        return super().get_object()

    def form_valid(self, form):
        fields = ['age','birth_date','phone_no','address','profile_pic']
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('hdps:profile-detail',kwargs={'pk':self.object.id})

def home(request):
    return render(request,'home.html')
