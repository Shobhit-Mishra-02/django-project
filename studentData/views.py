from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from studentData.forms  import StudentDetailsForm
from studentData.models import Student
import random
# from pymongo import MongoClient
# from django.conf import settings

# client = MongoClient('localhost',27017)
# db = client.studentDB
# Create your views here.


def index(request,):
    return render(request,'home.html')

def addStudentFrom(request):
    return render(request,"form.html")

def createStudent(request):
    print("creating student")

    if(request.method == 'POST'):
        firstName = request.POST["firstName"]
        lastName = request.POST["lastName"]
        age = request.POST["age"]
        location = request.POST["location"]
        
        
        Student(firstName=firstName, lastName=lastName, age=int(age), location=location).save()
        return HttpResponseRedirect("/")
        
    return HttpResponse("problem")

def showStudent(request):

    try:    
        firstName = request.GET['firstName']
        student = Student.objects.filter(firstName=firstName).values()
        # print(student[0])
        return render(request,"student.html",student[0])
    except:
        return render(request,'error.html')


def error(request):
    return render(request,'error.html')