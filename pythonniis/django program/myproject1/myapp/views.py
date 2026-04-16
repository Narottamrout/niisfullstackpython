from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')



def home1(request):
    return HttpResponse("hello sir")

def about1(request):
    return HttpResponse("This is About Page")

def contact(request):
    return HttpResponse("This is Contact Page")

def services(request):
    return HttpResponse("Our Services Page")

def welcome(request, name):
    return HttpResponse(f"Welcome {name}!") 


# Create your views here.
