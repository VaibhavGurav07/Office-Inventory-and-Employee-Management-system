from django.shortcuts import render, HttpResponse
from. models import Employee , Role, Department,Accesseries

# Create your views here.

def index(request):
    return  render(request,"employee/index.html")
    
def all_emp(request):
    emp = employee.objects.all()
    context={
        'emp': emp
    }
    return  render(request,"employee/all_emp.html",context)

def add_emp(request):
    return  render(request,"employee/add_emp.html")

def remove_emp(request):
    return  render(request,"employee/remove_emp.html")

def filter_emp(request):
    return  render(request,"employee/filter_emp.html")