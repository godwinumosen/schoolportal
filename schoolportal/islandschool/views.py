from django.shortcuts import render

from .models import Teacher, Student, Parent

def homepage(request):
    return render (request,'index.html')

def allteachers(request):
    teachers = Teacher.objects.order_by('-timestamp')
    context = {'teachers':teachers}
    return render(request, 'allteachers.html',context)

def allstudents (request):
    students = Student.objects.order_by('-timestamp')
    context = {'students':students}
    return render (request,'allstudents.html',context)

def student (request,slug):
    student = Student.objects.get(slug = slug)
    context = {'student':student}
    return render(request, 'student.html',context)

def parent (request,slug):
    parent = Parent.objects.get(slug = slug)
    context = {'parent':parent}
    return render(request, 'parent.html',context)

def login (request):
    return render(request, 'login.html')

def logout (request):
    return render (request, 'logout.html')

def signup (request):
    return render(request, 'signup.html')