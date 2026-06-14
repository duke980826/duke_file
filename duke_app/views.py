from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Student, Class
from weasyprint import HTML
# Create your views here.

def settings(_):
    return HttpResponse('setting page is waiting for implmentation')

def home(request):
    view_mode = request.GET.get('view' , 'student')
    
    if view_mode == 'class':
        classes = Class.objects.prefetch_related('students').all()
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
        
    
    
    return render(request, "home.html" ,context)

def student_receipt(request , pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request,"student_receipt.html" , {"student":student})

def student_receipt_pdf(request, pk):
    student = get_object_or_404(Student, pk=pk)
    html_string = render(
        request, "student_receipt.html", {"student": student, "pdf": True}
    ).content
    pdf = HTML(string=html_string, base_url=request.build_absolute_uri("/")).write_pdf()
    response = HttpResponse(pdf,  content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="receipt-{student.name}.pdf"'
    return response