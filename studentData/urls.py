from django.urls import path, include
from studentData import views

urlpatterns = [
    path("",views.index,name="home"),
    path("addStudent/",views.addStudentFrom, name="add student"),
    path("student/<int:id>",views.showStudent, name="student"),
    path("createStudent", views.createStudent, name="thanks page"),
]