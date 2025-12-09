from django.shortcuts import render,redirect
from .models import user
def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        address=request.POST.get('address')
        
        user.objects.create(username=username,email=email,password1=password1,password2=password2,address=address)
        
       # user1=user1(username=username,email=email,password1=password1,password2=password2,address=address)
        #user.save()
        return redirect('login')
    return render(request,'registration.html')              

def home(request):
    return render(request, 'landing.html')

def location(request):
    return render(request, 'location.html')

def login(request):
    return render(request, 'login.html')

def bookingappointment(request):
    return render(request, 'bookingappointment.html')

def medicalrecords(request):
    return render(request, 'medicalrecords.html')

def registration(request):
    return render(request,'registration.html')

def emergency(request):
    return render(request, 'emergency.html')

def hospitalavailable(request):
    return render(request,'hospitalavailable.html')

def ai_assisstance(request):
    return render(request, 'ai-assisstance.html')

def userprofile(request):
    return render(request, 'userprofile.html')

def started(request):
    return render(request, 'started.html')

def specialist(request):
    return render(request,'specialist.html')

def privacy(request):
    return render(request, 'privacy.html')

def termsofservice(request):
    return render(request, 'termsofservice.html')
def contactus(request):
    return render(request, 'contactus.html')
def aboutus(request):
    return render(request, 'aboutus.html')
