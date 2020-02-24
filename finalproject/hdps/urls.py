from django.contrib import admin
from django.urls import path
from hdps import views
from django.contrib.auth import views as auth_views

app_name = 'hdps'
urlpatterns = [
path('login/',auth_views.LoginView.as_view(template_name='signin.html'),name='login'),
path('signup/',views.SignUp.as_view(),name='user_signup'),
path('logout/',auth_views.LogoutView.as_view(),name='logout'),
path('profile/',views.ProfileForm.as_view(),name='profile_form')
]
