from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Employee
from .forms import AddRecordForm

def home(request):
    employee = Employee.objects.all()
    return render(request, 'home.html', {"Employee": employee})

def employeeData(request, pk):
    employeeData = Employee.objects.get(id=pk)
    return render(request, 'employee.html', {"Employee": employeeData})

def addEmployee(request, pk):
    employeeData = Employee.objects.get(id=pk)
    return render(request, 'addEmployee.html', {"Employee": addEmployee})

def employeeDelete(request, pk):
    ID = Employee.objects.get(id=pk)
    ID.delete()
    message.success(request, "Deleted Successfully")
    return redirect('home')

