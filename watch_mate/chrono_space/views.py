from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')    

def brand(request):
    return render(request,'brand.html')

def guide(request):   
    return render(request,'guide.html')     

def contact(request):
    return render(request,'contact.html')

def  contact(request):
    return render(request,'contact.html')  
    
def explore_now(request):
    return render(request,'shop.html') 

def login(request):
    return render(request,'login.html')           
  

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=make_password(password1))
        user.save()
        messages.success(request, "Signup successful! Please log in.")
        return redirect('login')  # You can create login page later

    return render(request, 'signup.html')
