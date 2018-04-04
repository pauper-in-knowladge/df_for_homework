from django.shortcuts import render
from register.models import *

# Create your views here.
def show_students(request):
    if request.method == 'POST':
        name = request.POST["username"]
        password = request.POST['password']
        email = request.POST['email']
        attr = request.POST['attr']
        class_name = request.POST['class_name']
        gender = request.POST['gender']
        authority = request.POST['authority']
        phone = request.POST['phone']

        student = Students()
        student.name = name
        student.pwd = password
        student.phone = phone
        student.email = email
        student.gender = gender
        student.class_name = class_name
        student.attr = attr
        student.authority = authority

        student.save()

    datas = Students.objects.all()

    return render(request,"student_management.html",{'datas':datas})

