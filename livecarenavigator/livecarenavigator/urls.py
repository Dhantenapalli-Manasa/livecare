"""
URL configuration for livecarenavigator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from livecareapp.views import register ,admin_registration,admin_login
from livecareapp.views import login_view,logout_view
from livecareapp.views import home,location
from livecareapp.views import home,login,bookingappointment,medicalrecords


from livecareapp.views import home,location,registration,hospitalavailable
from livecareapp.views import home,login,bookingappointment,emergency

from livecareapp.views import home,location,registration
from livecareapp.views import home,login,bookingappointment,emergency,ai_assisstance,userprofile,started
from livecareapp.views import home,login,bookingappointment,emergency,ai_assisstance


from livecareapp.views import home,location,registration,hospitalavailable
from livecareapp.views import home,login,bookingappointment,emergency
from livecareapp.views import home,location,registration,specialist
from livecareapp.views import home,login,bookingappointment,emergency,ai_assisstance,privacy,termsofservice,contactus,aboutus






    
   



urlpatterns =[
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),
    path('login/', login_view, name="login_view"),
    path('logout/', logout_view, name="logout"),
    path('admin_register/', admin_registration, name='admin_registration'),
    path('admin_login/', admin_login, name='admin_login'),
    

    path('home/',home),
    path('location/',location,name='location'),
    path('login/', login, name='login'),

    path('home/',home,name='home'),
    path('location/',location,name='location'),
    path('login/', login, name='login'),
    path('bookingappointment/', bookingappointment, name='bookingappointment'),
    path('medicalrecords/', medicalrecords, name='medicalrecords'),
    path('registration/',registration,name='registration'),
    path('emergency/', emergency, name='emergency'),

    path('hospitalavailable/',hospitalavailable,name='hospitalavailable'),

    path('ai-assisstance/', ai_assisstance, name='ai-assisstance'),

    path('user/', userprofile, name='userprofile'),
    path('started/', started, name='started'),
    path('specialist/',specialist,name='specialist'),
    path('privacy/', privacy, name='privacy'),
    path('terms-of-service/', termsofservice, name='termsofservice'),
    path('contact-us/', contactus, name='contactus'),
    path('about-us/', aboutus, name='aboutus'),
]
