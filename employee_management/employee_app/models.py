from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)
    lacation = models.CharField(max_length=100)

class Role(models.Model):
    name = models.CharField(max_length=100,null=False)

class Accesseries(models.Model):
    name = models.CharField(max_length=50, null= False)


class Employee(models.Model):
    first_name = models.CharField(max_length=100, null = False)
    last_name = models.CharField(max_length=100)
    dept = models.ForeignKey(Department,on_delete = models.CASCADE)
    salary = models.IntegerField(default= 0)
    email = models.EmailField(max_length=100,null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    hire_date = models.DateField()
    assign = models.ForeignKey(Accesseries,on_delete=models.CASCADE)