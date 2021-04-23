from django.shortcuts import render, redirect

from onetomany.forms import DepartmentForm, EmployeeForm
from onetomany.models import Department, Employee


def home(request):
    return render(request, 'onetomany/home.html', {'hometext': 'One To Many'})

def department(request):
    return render(request, 'onetomany/department.html', {'departmentpage': 'Department'})

def departmentshow(request):
    list = Department.objects.all()
    return render(request, 'onetomany/departmentshow.html', {'list': list})

def departmentadd(request):
    if request.method == 'POST':
        department = DepartmentForm(request.POST)
        department.save()
        return redirect('/onetomany/department/show')
    else:
        form = DepartmentForm
        return render(request, 'onetomany/departmentadd.html', {'form': form})

def departmentdelete(request, id):
    department = Department.objects.get(id=id)
    department.delete()
    return redirect('/onetomany/department/show')

def departmentview(request, id):
    dep = Department.objects.get(id=id)
    return render(request, 'onetomany/departmentview.html', {'dep': dep, 'departmentpage': 'Department'})

def employee(request):
    return render(request, 'onetomany/employee.html', {'employeepage': 'Employee'})

def employeeadd(request):
    if request.method == 'POST':
        employee = EmployeeForm(request.POST)
        employee.save()
        return redirect('/onetomany/employee/show')
    else:
        form = EmployeeForm
        return render(request, 'onetomany/employeeadd.html', {'form': form})

def employeeshow(request):
    list = Employee.objects.all()
    return render(request, 'onetomany/employeeshow.html', {'list': list})

def employeeview(request, id):
    emp = Employee.objects.get(id=id)
    return render(request, 'onetomany/employeeview.html', {'emp': emp})

def employeedelete(request, id):
    emp = Employee.objects.get(id=id)
    emp.delete()
    return redirect('/onetomany/employee/show')

def employeeupdate(request, id):
    if request.method == 'POST':
        emp = Employee.objects.get(id=id)
        employee = EmployeeForm(request.POST, instance=emp)
        employee.save()
        return redirect('/onetomany/employee/show')
    else:
        emp = Employee.objects.get(id=id)
        dep = Department.objects.all()
        return render(request, 'onetomany/employeeupdate.html', {'emp': emp, 'dep': dep})








# Create your views here.
