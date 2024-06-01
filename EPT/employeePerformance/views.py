from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Employee
from .forms import addEmployeeForm

def home(request):
    employee = Employee.objects.all()
    return render(request, 'home.html', {"Employee": employee})

def about(request):
    return render(request, 'about.html', {})

def updateEmployee(request, pk):
    employeeData = Employee.objects.get(id=pk)
    form = addEmployeeForm(request.POST or None, instance = employeeData)
    if form.is_valid():
        form.save()
        messages.success(request, "Employee Data has Been Updated!")
        return redirect('home')
    else:
        return render(request, 'employee.html', {'form':form})

def addEmployee(request):
    form = addEmployeeForm(request.POST or None)
    if request.method == 'POST':
        form = addEmployeeForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home') 
    return render(request, 'addEmployee.html', {'form':form})

def employeeDelete(request, pk):
    ID = Employee.objects.get(id=pk)
    ID.delete()
    messages.success(request, "Deleted Successfully")
    return redirect('home')