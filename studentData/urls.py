from django.urls import path, include
from studentData import views

urlpatterns = [
    path("",views.index,name="home"),
    path("addStudent/",views.addStudentFrom, name="add student"),
    path("student",views.showStudent, name="student"),
    path("createStudent", views.createStudent, name="thanks page"),
    path('error/', views.error, name='error page')
]