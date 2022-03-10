from django.shortcuts import render, redirect
from .models import Employee


def home_page(request):
    if request.method == "POST":
        # print(request.POST)
        data = {k:request.POST[k] for k in request.POST}
        data.pop("csrfmiddlewaretoken")
        
        Employee.objects.create(**data)
        
        
        return redirect("aboutpage")
    
    context = {
        "section" : "home"
    }
    
    return render(request, "home.html", context=context)


def about_page(request):
    
    all_emp = Employee.objects.all()
    
    data = {
        "section" : "about",
        "employees" : all_emp
    }
    
    return render(request, "about.html", context=data)


def employee_detail(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    
    data = {
        "section" : "about",
        "employee" : employee
    }
    
    return render(request, "employee.html", context=data)
    
    