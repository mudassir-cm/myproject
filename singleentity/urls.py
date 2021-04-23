from django.urls import path
from singleentity import views

urlpatterns = [
    path('home', views.home),
    path('person/show', views.peronshow),
    path('person/add', views.personadd),
    path('person/update/<int:id>', views.personupdate),
    path('person/delete/<int:id>', views.persondelete),
    path('person/view/<int:id>', views.personview),
]