from django.shortcuts import render
from django.http import HttpResponse
from studentData.models import Student

# This controller display the home page. 
def index(request):
    return render(request,'home.html')

# This controller display the student registration form.
def addStudentFrom(request):
    return render(request,"form.html")

# This controller creates a new student in the mongodb database.
def createStudent(request):

    if(request.method == 'POST'):
        firstName = request.POST["firstName"]
        lastName = request.POST["lastName"]
        age = request.POST["age"]
        location = request.POST["location"]
        
        
        student = Student(firstName=firstName, lastName=lastName, age=int(age), location=location)
        student.save()
        return render(request,'formSubmitted.html',{"id":student.id})
        
    return HttpResponse("problem")

# This controller display the student details, if the student is registered.
def showStudent(request):

    try:    
        id = request.GET['id']
        student = Student.objects.filter(id=id).values()
        print(student[0])
        return render(request,"student.html",student[0])
    except:
        return render(request,'error.html')

