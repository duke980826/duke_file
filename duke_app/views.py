from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def settings(_):
    return HttpResponse('setting page is waiting for implmentation')

def home(request):
    return render(request, "home.html")

