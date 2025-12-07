from django.shortcuts import render
def home(request):
    return render(request,'landing.html')
def login(request):
    return render(request,'login.html')

# Create your views here.
