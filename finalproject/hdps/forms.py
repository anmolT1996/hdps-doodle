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
        model = Profile
        # fields = '__all__
        exclude = ['user']

class UserReportForm(forms.Form):
    SEX_CHOICES = [
        (1,'Male'),
        (0,'Female'),
        (0,'Others')
    ]
    CHEST_PAIN_CHOICES = [
        (1,'Typical Angina'),
        (2,'Atypical Angina'),
        (3,'Non-Anignal Pain'),
        (4,'Asymptotic')
    ]
    BLOOD_SUGAR_CHOICES = [
        (0,'Blood Sugar < 120mg/dl'),
        (1,'Blood Sugar > 120mg/dl')
    ]
    ECG_CHOICES = [
        (0,'Normal'),
        (1,'Having ST-T Wave Abromality'),
        (2,'Left Ventricular Hyperthrophy')
    ]
    EXERCISE_ANGINA_CHOICES = [
        (1,'Yes'),
        (0,'No')
    ]
    PEAK_ST_SEGMENT_CHOICES = [
        (1,'Upsloping'),
        (2,'Flat'),
        (3,'Downsloping')
    ]
    THAL_CHOICES=[
        (3,'Normal'),
        (6,'Fixed Defect'),
        (7,'Reversible Defect')
    ]
    age = forms.IntegerField()
    sex = forms.ChoiceField(choices= SEX_CHOICES)
    cp = forms.ChoiceField(choices= CHEST_PAIN_CHOICES)
    # restbps = forms.IntegerField()
    chol = forms.IntegerField()
    fbs = forms.ChoiceField(choices=BLOOD_SUGAR_CHOICES)
    # ecg = forms.IntegerField(choices=ECG_CHOICES)
    # heart_rate = forms.IntegerField()
    ex_in_angina = forms.ChoiceField(choices = EXERCISE_ANGINA_CHOICES)
    st_depression_in_exercise = forms.FloatField()
    peak_st_segment = forms.ChoiceField(choices=PEAK_ST_SEGMENT_CHOICES)
    vessels_by_flourosopy = forms.FloatField()
    thal = forms.ChoiceField(choices=THAL_CHOICES)
