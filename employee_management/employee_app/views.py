from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return  render(request,"employee/index.html")
    
def all_emp(request):
    return  render(request,"employee/all_emp.html")

def add_emp(request):
    return  render(request,"employee/add_emp.html")

def remove_emp(request):
    return  render(request,"employee/remove_emp.html")

def filter_emp(request):
    return  render(request,"employee/filter_emp.html")