from django.shortcuts import render, redirect

from school.form import StudentForm, TeacherForm
from school.models import Student, Teacher


def schoolmainpage(request):
    return render(request, 'school/schoolmainpage.html')

def studentcreate(request):
    form = StudentForm
    return render(request, 'school/studentcreate.html', {'form': form})

def studentadd(request):
    form = StudentForm(request.POST)
    form.save()
    return redirect('/school/student/show')

def studentshow(request):
    list = Student.objects.all()
    return render(request, 'school/studentshow.html', {'list': list})

def studentedit(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'school/studentedit.html', {'student': student})

def studentdelete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/school/student/show')

def studentupdate(request, id):
    student = Student.objects.get(id=id)
    std = StudentForm(request.POST, instance=student)
    std.save()
    return redirect('/school/student/show')

def teachercreate(request):
    form = TeacherForm
    return render(request, 'school/teachercreate.html', {'form': form})

def teacheradd(request):
    teacher = TeacherForm(request.POST)
    teacher.save()
    return redirect('/school/teacher/show')

def teachershow(request):
    list = Teacher.objects.all()
    return render(request, 'school/teachershow.html', {'list': list})

def teacherdelete(request, id):
    teacher = Teacher.objects.get(id=id)
    teacher.delete()
    return redirect('/school/teacher/show')

def teacheredit(request, id):
    teacher = Teacher.objects.get(id=id)
    return render(request, 'school/teacheredit.html', {'teacher': teacher})

def teacherupdate(request, id):
    tr = Teacher.objects.get(id=id)
    teacher = TeacherForm(request.POST, instance=tr)
    teacher.save()
    return redirect('/school/teacher/show')
# Create your views here.
