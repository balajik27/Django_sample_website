from pyexpat import model
from django.contrib import admin
from lecture1.models import Employee
# from django.db.models import Model
# Register your models here.
# admin.autodiscover()
class Employeeadmin(admin.ModelAdmin):
    emp_details = ['empno','empname','empsalary','empaddress']
    
admin.site.register(Employee , Employeeadmin)
