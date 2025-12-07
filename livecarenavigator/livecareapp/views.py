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

def registration(request):
    return render(request,'registration.html')
def emergency(request):
    return render(request, 'emergency.html')
<<<<<<< HEAD
def hospitalavailable(request):
    return render(request,'hospitalavailable.html')
=======
def ai_assisstance(request):
    return render(request, 'ai-assisstance.html')
>>>>>>> 83893ee71238d846f68f1e957b9c27be9bc3fe38
