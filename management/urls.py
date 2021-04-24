from django.urls import path

from management import views

urlpatterns = [
    path('managementmainpage', views.managementmainpage),
    path('employee/create', views.employeecreate),
    path('employee/add', views.employeeadd),
    path('employee/show', views.employeeshow),
    path('employee/delete/<int:id>', views.employeedelete),
    path('employee/edit/<int:id>', views.employeeedit),
    path('employee/update/<int:id>', views.employeeupdate),
    path('project/create', views.projectcreate),
    path('project/add', views.projectadd),
    path('project/show', views.projectshow),
    path('project/delete/<int:id>', views.projectdelete),
    path('project/edit/<int:id>', views.projectedit),
    path('project/update/<int:id>', views.projectupdate)


]