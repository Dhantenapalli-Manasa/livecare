from django.shortcuts import render, redirect
from .models import user,AdminUser    
from django.contrib import messages
from django.contrib.auth.hashers import check_password  

def register(request): 
    if request.method == 'POST':
       username = request.POST.get('username')
       email = request.POST.get('email')
       password1 = request.POST.get('password1')
       password2 = request.POST.get('password2')
       address = request.POST.get('address')
       user.objects.create(
           username=username,email=email, password1=password1,
           password2=password2,address=address)
       return redirect('login')
    return render(request, 'registration.html')





def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Check if email exists
        try:
            user = user.objects.get(username=username)
        except user.DoesNotExist:
            messages.error(request, "Invalid email or password")
            return redirect("login")

        # Validate password
        if check_password(password, user.password):
            # Create session
            request.session["user_id"] = user.id
            request.session["username"] = user.username
            return redirect("home")  # change where you want
        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")

    return render(request, "login.html")
def logout_view(request):
    request.session.flush()
    return redirect("login")

def admin_registration(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        AdminUser.objects.create(
            username=username,
            email=email,
            password=password
        )

        return redirect("admin_login")  # You can create admin login view later

    return render(request, "admin_registration.html")   
def admin_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            admin = AdminUser.objects.get(email=email)

            if admin.password == password:
                # store session
                request.session["admin_id"] = admin.id
                request.session["admin_username"] = admin.username
                
                messages.success(request, "Login successful!")
                return redirect("home")    # redirect to admin dashboard
            else:
                messages.error(request, "Incorrect password.")
                return redirect("admin_login")

        except AdminUser.DoesNotExist:
            messages.error(request, "Admin with this email does not exist.")
            return redirect("admin_login")

    return render(request, "admin_login.html")
def admin_logout(request):
    request.session.flush()
    return redirect("admin_login")



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

