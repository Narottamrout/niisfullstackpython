from django.http import HttpResponse

# Create your views here.
def home(request):
	return HttpResponse("hello django")

def home(request):
    return HttpResponse("This is Home Page")

def about(request):
    return HttpResponse("This is About Page")

def contact(request):
    return HttpResponse("This is Contact Page")
def contact(request):
    return HttpResponse("our services")
def welcome(request,name):
	return HttpResponse(f"welcome{name}!")  
	  

