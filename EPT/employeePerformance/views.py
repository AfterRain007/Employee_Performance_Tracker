from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Employee
from .forms import AddRecordForm

def home(request):
    employee = Employee.objects.all()
    return render(request, 'home.html', {"Employee": employee})

def updateEmployee(request, pk):
    employeeData = Employee.objects.get(id=pk)
    form = AddRecordForm(request.POST or None, instance = employeeData)
    if form.is_valid():
        form.save()
        messages.success(request, "Employee Data has Been Updated!")
        return redirect('home')
    else:
        return render(request, 'employee.html', {'form':form})

def addEmployee(request, pk):
    employeeData = Employee.objects.get(id=pk)
    return render(request, 'addEmployee.html', {"Employee": addEmployee})

def employeeDelete(request, pk):
    ID = Employee.objects.get(id=pk)
    ID.delete()
    messages.success(request, "Deleted Successfully")
    return redirect('home')

