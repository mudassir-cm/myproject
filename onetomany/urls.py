from django.urls import path
from onetomany import views

urlpatterns = [
    path('home', views.home),
    path('department', views.department),
    path('department/show', views.departmentshow),
    path('department/add', views.departmentadd),
    path('department/delete/<int:id>', views.departmentdelete),
    path('department/view/<int:id>', views.departmentview),
    path('employee', views.employee),
    path('employee/add', views.employeeadd),
    path('employee/show', views.employeeshow),
    path('employee/view/<int:id>', views.employeeview),
    path('employee/delete/<int:id>', views.employeedelete),
    path('employee/update/<int:id>', views.employeeupdate)
]