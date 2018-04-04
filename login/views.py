from django.shortcuts import render

# Create your views here.
def login(request):
    data = {}
    return render(request,"login.html",data)