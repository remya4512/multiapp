from django.shortcuts import render

# Create your views here.
def app3home(request):
    return render(request,'home1.html')
def details(request):
    return render(request,'details.html')
def register(request):
    return render(request,'register.html')