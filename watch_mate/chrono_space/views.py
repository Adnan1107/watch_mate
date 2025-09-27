from django.shortcuts import render

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