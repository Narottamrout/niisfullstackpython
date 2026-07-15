from django.shortcuts import render, redirect
from .models import Student

def index(request):
    students = Student.objects.all()
    return render(request, "students/index.html", {"students": students})


def add_student(request):
    if request.method == "POST":
        Student.objects.create(
            name=request.POST['name'],
            roll_number=request.POST['roll']
        )
    return redirect('index')


def delete_student(request, id):
    Student.objects.get(id=id).delete()
    return redirect('index')


def edit_student(request, id):
    student = Student.objects.get(id=id)
    return render(request, "students/edit.html", {"student": student})


def update_student(request, id):
    student = Student.objects.get(id=id)
    student.name = request.POST['name']
    student.roll_number = request.POST['roll']
    student.save()
    return redirect('index')