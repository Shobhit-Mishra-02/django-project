from django.shortcuts import render
from django.http import HttpResponse
from studentData.forms  import StudentDetailsForm
from pymongo import MongoClient

client = MongoClient('localhost',27017)
db = client.studentDB
# Create your views here.

def index(request,):
    return render(request,'home.html')

def addStudentFrom(request):
    return render(request,"form.html")

def createStudent(request):
    print("creating student")

    if(request.method == 'POST'):
        form = StudentDetailsForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            db.students.insert_one(form.cleaned_data)

            return HttpResponse('done')
        
    return HttpResponse("problem")

def showStudent(request, id):
    return render(request,"student.html")