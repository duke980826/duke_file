from django.contrib import admin
from .models import Student,Class

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["student_id",  "name", "grade", "phone" , "amount_due"]

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ["name", "student_count"]

    @admin.display(description="Student Number")
    def student_count(self, obj):
        return obj.students.count()