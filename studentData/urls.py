from django.urls import path
from studentData import views

urlpatterns = [
    path("",views.index,name="home"),
    path("addStudent/",views.addStudentFrom, name="add student"),
    path("student",views.showStudent, name="student"),
    path("createStudent", views.createStudent, name="creating student"),
]