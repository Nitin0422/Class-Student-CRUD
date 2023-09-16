from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Class, Student
from .forms import ClassForm, StudentForm

# Create your views here.
def index(request):
    class_list = Class.objects.all()
    context = {"class_list": class_list}
    return render(request, "school/index.html", context)

def addClass(request):
    if request.method == "POST":
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    else:
        form = ClassForm()

    return render(request, 'school/class/add_class.html', {'form': form})

def editClass(request, class_id):
    class_ = get_object_or_404(Class, pk=class_id)

    if request.method == "POST":
        form = ClassForm(request.POST, instance=class_)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ClassForm(instance=class_)
    return render(request, 'school/class/edit_class.html', {'form': form})

def deleteClass(request, class_id):
    class_to_delete = get_object_or_404(Class, pk=class_id)
    if request.method == "POST":
        class_to_delete.delete()
        return redirect('/')
    return render(request, "school/class/confirm.html", {"class": class_to_delete})

def showStudents(request, class_id):
    class_instance = get_object_or_404(Class, pk=class_id)
    students = class_instance.student_set.all()
    return render(request, "school/student_list.html", {"class_instance": class_instance, "students": students})


def editStudent(request, student_id, class_id):
    student_instance = get_object_or_404(Student, pk=student_id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance = student_instance, class_instance= class_id )
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = StudentForm(instance = student_instance)
    return render(request, "school/student/edit_student.html", {"form":form})

def addStudent(request, class_id):
    class_instance = get_object_or_404(Class, pk=class_id)
    if request.method == "POST":
        form = StudentForm(request.POST, class_instance = class_instance)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = StudentForm(class_instance=class_instance)
    return render(request, 'school/student/add_student.html', {'form':form})

def deleteStudent(request, student_id):
    student_instance = get_object_or_404(Student, pk=student_id)
    if request.method == "POST":
        student_instance.delete()
        return redirect('/')
    return render(request, "school/student/confirm.html", {"student":student_instance})