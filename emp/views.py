from django.shortcuts import render,redirect
from .models import Employee

# Create your views here.
def allemployees(request):
    emp=Employee.objects.all()
    return render(request, "emp/allemployees.html", {"allemployees":emp})

def singleemployee(request, empid):
    return render(request, "emp/singleemployee.html")

def addemployee(request):
    #take all the parameters from form- by their names kept
    if request.method=="POST":
        employee_id=request.POST.get('employee_id')   #get the same names as mentioned in 'name' tag from addemployee page
        employee_name=request.POST.get('employee_name')
        employee_email=request.POST.get('employee_email')
        employee_address=request.POST.get('employee_address')
        employee_phone=request.POST.get('employee_phone')

        #create object for models
        e=Employee()
        e.employee_id=employee_id   #left name should be from models object and assign value from POST method
        e.Name=employee_name
        e.email=employee_email
        e.address=employee_address
        e.phone_nuber=employee_phone
        e.save()
        return redirect("/allemployees")

    return render(request, "emp/addemployee.html")

def deleteemployee(request, empid):
    e=Employee.objects.get(pk=empid)
    e.delete()
    return redirect("allemployees")

def updateemployee(request, empid):
    e=Employee.objects.get(pk=empid)
    

    return render(request, "emp/updateemployee.html",{'singleemp':e})

def doupdateemployee(request,empid):
        updatedemployee_id=request.POST.get('employee_id')   #get the same names as mentioned in 'name' tag from addemployee page
        upadtedemployee_name=request.POST.get('employee_name')
        updatedemployee_email=request.POST.get('employee_email')
        updatedemployee_address=request.POST.get('employee_address')
        updatedemployee_phone=request.POST.get('employee_phone')

        #create object for models
        e=Employee.objects.get(pk=empid)
        e.employee_id=updatedemployee_id   #left name should be from models object and assign value from POST method
        e.Name=upadtedemployee_name
        e.email=updatedemployee_email
        e.address=updatedemployee_address
        e.phone_nuber=updatedemployee_phone
        e.save()
        return redirect("allemployees")




