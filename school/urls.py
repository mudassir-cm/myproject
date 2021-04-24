from django.urls import path

from school import views

urlpatterns = [
    path('schoolmainpage/', views.schoolmainpage),
    path('student/create/', views.studentcreate),
    path('student/add', views.studentadd),
    path('student/show', views.studentshow),
    path('student/delete/<int:id>', views.studentdelete),
    path('student/edit/<int:id>', views.studentedit),
    path('student/update/<int:id>', views.studentupdate),
    path('teacher/create/', views.teachercreate),
    path('teacher/add/', views.teacheradd),
    path('teacher/show/', views.teachershow),
    path('teacher/delete/<int:id>', views.teacherdelete),
    path('teacher/edit/<int:id>', views.teacheredit),
    path('teacher/update/<int:id>', views.teacherupdate),
]