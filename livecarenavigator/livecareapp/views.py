from django.shortcuts import render
def home(request):
    return render(request,'landing.html')
def location(request):
    return render(request,'location.html')

# Create your views here.
