from django.shortcuts import render, HttpResponse
from. models import Employee , Role, Department,Accesseries
from datetime import datetime

# Create your views here.

def index(request):
    return render(request,"employee/index.html")
    

def all_emp(request):
    emp = Employee.objects.all()
    context={
        'emp': emp
    }
    return  render(request,"employee/all_emp.html",context)


def add_emp(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = int(request.POST['dept'])
        salary = int(request.POST['salary'])
        email = request.POST['email']
        role = int(request.POST['role'])
        phone = int(request.POST['phone'])
        hire_date = request.POST['hire_date']
        assign = int(request.POST['assign'])
        new_emp = Employee(first_name=first_name,last_name=last_name,dept_id=dept,salary=salary,email=email,role_id=role,phone=phone,hire_date=datetime.now(),assign_id=assign)
        new_emp.save()
        return HttpResponse("employee Add successfully")
    else:
        return render(request,"employee/add_emp.html")


def remove_emp(request):
    return  render(request,"employee/remove_emp.html")


def filter_emp(request):
    return  render(request,"employee/filter_emp.html")