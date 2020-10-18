from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print("Accessed by: ", request.user)
    #return HttpResponse("<h1>Hello World !!!</h1>")
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Contact Us</h1>")
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    #return HttpResponse("<h1>About Us</h1>")
    return render(request, "about.html", {})

def social_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Connect With Us</h1>")
    return render(request, "social.html", {})