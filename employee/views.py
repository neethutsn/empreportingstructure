from django.shortcuts import render,redirect
from . models import *

# Create your views here.


def homepage(request):
    return render(request,"home.html")

def loginpage(request):
    if request.method == "POST":
        ecode = request.POST['emp']
        pwd = request.POST['password']
        try:
            user = User.objects.get(emp_code = ecode,emp_pwd = pwd)
            request.session['user_empcode'] = user.id
            if (user.emp_code == "emp01" or user.emp_code == "emp06"):
                return redirect('superdash')
            else:
                return redirect('viewemployees')

           
        except User.DoesNotExist:
            return render(request,'login.html',{'msg':'login failed'})
        
    return render(request,"login.html")

def registerpage(request):
    message = ""
    user_data = ""
    if request.method == "POST":
        user_name = request.POST['name']
        user_contact = request.POST['contact']
        user_category = request.POST['category']
        user_pwd = request.POST['password']
        user_empcode = request.POST['empcode']
        if (user_empcode == 'emp02' or user_empcode == 'emp03' or user_empcode == 'emp04' or user_empcode == 'emp05'):
            user_data = User(emp_name = user_name,emp_contact = user_contact,emp_cat = user_category,emp_code = user_empcode,emp_pwd = user_pwd,emp_supervisor = "emp01")
            user_data.save()

        elif(user_empcode == 'emp07' or user_empcode == 'emp08' or user_empcode == 'emp09' or user_empcode == 'emp10'):
            user_data = User(emp_name = user_name,emp_contact = user_contact,emp_cat = user_category,emp_code = user_empcode,emp_pwd = user_pwd,emp_supervisor = "emp06")
            user_data.save()

        else:
            user_data = User(emp_name = user_name,emp_contact = user_contact,emp_cat = user_category,emp_code = user_empcode,emp_pwd = user_pwd)
            user_data.save()
           
        if user_data:
            message = "Data inserted successfully"
        else:
            message = "error"   
    return render(request,"signup.html",{'msg':message})

def dashpage(request):
    return render(request,"dashboard.html")

def employeepage(request):
    employees = User.objects.all()
    return render(request,"viewemployees.html",{'emp_data':employees})

def supervisorpage(request):
    employees = User.objects.all()
    return render(request,"superdash.html",{'emp_data':employees})

def logoutpage(request):
    del request.session['user_empcode']
    return redirect('login')