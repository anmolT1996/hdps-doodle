from django.contrib.auth  import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib import auth
from hdps.models import Profile
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length = 256)
    last_name = forms.CharField(max_length = 256)
    class Meta:
        fields = ('username','first_name','last_name','email','password1','password2')
        model = get_user_model()

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            self.fields['username'].label = 'USER NAME'
            self.fields['first_name'].label = 'FIRST NAME'
            self.fields['last_name'].label = 'LAST NAME'
            self.fields['email'].label = 'EMAIL'
            self.fields['password1'].label = 'PASSWORD'
            self.fields['password2'].label = 'CONFORM PASSWORD'

class ProfileModelForm(forms.ModelForm):
    class Meta:
        fields ='__all__'
        model = Profile
    
