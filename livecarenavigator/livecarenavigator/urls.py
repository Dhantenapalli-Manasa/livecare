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
from livecareapp.views import home,location
from livecareapp.views import home,login,bookingappointment,medicalrecords
from livecareapp.views import home,location,registration
from livecareapp.views import home,login,bookingappointment,emergency,ai_assisstance
urlpatterns =[
    path('admin/', admin.site.urls),

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
    path('ai-assisstance/', ai_assisstance, name='ai-assisstance'),

]
