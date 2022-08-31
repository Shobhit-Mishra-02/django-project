from cProfile import label
from django import forms

class StudentDetailsForm(forms.Form):
    firstName = forms.CharField(label="First name",max_length=100)
    lastName = forms.CharField(label="Last name", max_length=100)
    age = forms.IntegerField()
    location = forms.CharField(label="location", max_length=200)