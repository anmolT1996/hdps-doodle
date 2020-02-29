from django.db import models
from django.conf import settings
from django.contrib import auth
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
# Create your models here.
class User(auth.models.User,auth.models.PermissionsMixin):
    def __str__(self):
        return '{} {}'.format(self.first_name,self.last_name)

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    age = models.IntegerField(blank=True,null=True)
    birth_date = models.DateField(null=True, blank=True)
    phone_no = models.IntegerField()
    address = models.CharField(max_length=30, blank=True)
    profile_pic = models.ImageField(blank=True,null=True)

    def __str__(self):
        return " {} ".format(self.user)

    # def get_absolute_url(self):
    #     return reverse('hdps:profile-detail', kwargs={'pk': self.pk})

def post_save_user_model_reciever(sender,instance,created,*args,**kwargs):
    if created:
        try:
            Profile.objects.create(user=instance)
        except:
            pass
post_save.connect(post_save_user_model_reciever,sender=settings.AUTH_USER_MODEL)



#
# @receiver(post_save, sender=auth.models.User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
# @receiver(post_save, sender=auth.models.User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
