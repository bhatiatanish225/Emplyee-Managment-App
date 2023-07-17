from django.http import HttpResponse
from django.shortcuts import render,redirect
from details.models import Employee_details


def emp_home(request):
    emps=Employee_details.objects.all()
    return render(request,'home.html',{'emps':emps})

def add_emp(request):
    if request.method=='POST':
        emp_name=request.POST.get('emp_name')
        emp_positions=request.POST.get('emp_positions')
        emp_department=request.POST.get('emp_department')
        emp_phone=request.POST.get('emp_phone')
        emp_address=request.POST.get('emp_address')
        emp_email=request.POST.get('emp_email')
        
        
        e=Employee_details()
        e.name=emp_name
        e.phone=emp_phone
        e.address=emp_address
        e.deparment=emp_department
        e.positions=emp_positions
        e.email=emp_email
        e.save()
        print('data is coming')
        return redirect('/')
   
    return render(request,'add_emp.html',{})