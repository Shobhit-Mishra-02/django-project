import imp
from django.contrib import admin
from studentData import models

# Register your models here.
admin.site.register(models.Student)