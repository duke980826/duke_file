from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Class
# Create your views here.

def settings(_):
    return HttpResponse('setting page is waiting for implmentation')

def home(request):
    view_mode = request.GET.get('view' , 'student')
    
    if view_mode == 'class':
        classes = Class.objectss.prefetch_related('students').all()
        context = {
            'view_mode': 'class',
            'classes': classes,
        }
    else:
        students = Student.objects.all().order_by("student_id")
        context ={
            "view_mode": "student",
            "students": students,
        }
        
    
    
    return render(request, "home.html")

