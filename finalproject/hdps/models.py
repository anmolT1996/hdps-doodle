from django.db import models
from django.conf import settings
from django.contrib import auth
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils import timezone
# Create your models here.
class User(auth.models.User,auth.models.PermissionsMixin):
    def __str__(self):
        return '{} {}'.format(self.first_name,self.last_name)

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key = True,on_delete=models.CASCADE)
    age = models.IntegerField(blank=True,null=True)
    birth_date = models.DateField(null=True, blank=True)
    phone_no = models.IntegerField()
    address = models.CharField(max_length=30, blank=True)
    profile_pic = models.ImageField(blank=True,null=True)

    def __str__(self):
        return " {} ".format(self.user)

    # def get_absolute_url(self):
    #     return reverse('hdps:profile-detail', kwargs={'pk': self.pk})


class UserReport(models.Model):
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
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    age = models.IntegerField()
    sex = models.IntegerField(choices= SEX_CHOICES)
    cp = models.IntegerField(choices= CHEST_PAIN_CHOICES)
    restbps = models.IntegerField()
    chol = models.IntegerField()
    fbs = models.IntegerField(choices=BLOOD_SUGAR_CHOICES)
    ecg = models.IntegerField(choices=ECG_CHOICES)
    heart_rate = models.IntegerField()
    ex_in_angina = models.IntegerField(choices = EXERCISE_ANGINA_CHOICES)
    st_depression_in_exercise = models.FloatField()
    peak_st_segment = models.IntegerField(choices=PEAK_ST_SEGMENT_CHOICES)
    vessels_by_flourosopy = models.FloatField()
    thal = models.IntegerField(choices=THAL_CHOICES)
    date_time = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return "{}".format(self.user)

def post_save_user_model_reciever(sender,instance,created,*args,**kwargs):
    if created:
        try:
            Profile.objects.create(user=instance)
        except:
            pass
post_save.connect(post_save_user_model_reciever,sender=settings.AUTH_USER_MODEL)
