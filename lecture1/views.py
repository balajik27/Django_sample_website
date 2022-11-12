from email import message
import imp
from django.shortcuts import render
from lecture1.models import Employee #now employee is a class 
# Create your views here.
from . import forms

import datetime
def hello(request):
    # message = "hi "
    # date = datetime.datetime.now()
    # hour = int(date.strftime("%H"))
    # if hour >12:
    #     message+= "good morning"

    # else:
    #     message+= "good afternoon"
    # name = "balaji"
    # date_dict={'display_date' : date , "name" : name , "greeting" : message}
    #context=date_dict


    # emp_data = Employee.objects.all() #query set .. take all the data
    # emp_dict = {'emp_list':emp_data}
    # return render(request,'index.html',context=emp_dict)

    form = forms.Employeeinfo()
    empinfo = {'form':form}
    return render(request,'form_temp.html',context=empinfo)

def db_values(request):
    if request.method == "POST":
        Emp = Employee()  #creating object for that class
        Emp.empno = request.POST.get('no')
        Emp.empname = request.POST.get('name')
        Emp.empaddress = request.POST.get('address')
        Emp.empsalary = request.POST.get('salary')
        Emp.save()
    return render(request,'form_temp.html',{'ack' : "successfully stored"})