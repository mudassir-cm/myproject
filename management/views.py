from django.shortcuts import render, redirect

from management.form import EmployeeForm, ProjectForm
from management.models import Employee, Project


def managementmainpage(request):
    return render(request, 'management/managementmainpage.html')

def employeecreate(request):
    form = EmployeeForm
    return render(request, 'management/employeecreate.html', {'form': form})

def employeeadd(request):
    emp = EmployeeForm(request.POST)
    emp.save()
    return redirect('/management/employee/show')

def employeeshow(request):
    list = Employee.objects.all()
    return render(request, 'management/employeeshow.html', {'list': list})

def employeedelete(request, id):
    emp = Employee.objects.get(id=id)
    emp.delete()
    return redirect('/management/employee/show')

def employeeedit(request, id):
    emp = Employee.objects.get(id=id)
    return render(request, 'management/employeeedit.html', {'emp': emp})

def employeeupdate(request, id):
    emp = Employee.objects.get(id=id)
    employee = EmployeeForm(request.POST, instance=emp)
    employee.save()
    return redirect('/management/employee/show')

def projectcreate(request):
    project = ProjectForm
    return render(request, 'management/projectcreate.html', {'project': project})

def projectadd(request):
    project = ProjectForm(request.POST)
    project.save()
    return redirect('/management/project/show')

def projectshow(request):
    list = Project.objects.all()
    return render(request, 'management/projectshow.html', {'list': list})

def projectdelete(request, id):
    pro = Project.objects.get(id=id)
    pro.delete()
    return redirect('/management/project/show')

def projectedit(request, id):
    project = Project.objects.get(id=id)
    return render(request, 'management/projectedit.html', {'project': project})

def projectupdate(request, id):
    pro = Project.objects.get(id=id)
    project = ProjectForm(request.POST, instance=pro)
    project.save()
    return redirect('/management/project/show')




# Create your views here.
