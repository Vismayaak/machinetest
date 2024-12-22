from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.
def employee_list(request):
    employees=Employee.objects.all()
    return render(request,'employee_list.html',{'employees':employees})
def add_employee(request):
    if request.method=='POST':
        form=EmpForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form=EmpForm()
    return render(request,'add_employee.html',{'form':form})
def delete_employee(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('employee_list')
def update_employee(request):
    if request.method=='POST':
        form=EmpForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form=EmpForm()
    return render(request,'add_employee.html',{'data':form})

        