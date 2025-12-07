from django.shortcuts import render
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
