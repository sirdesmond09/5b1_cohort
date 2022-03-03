from django.shortcuts import render, redirect


def home_page(request):
    if request.method == "POST":
        print(request.POST)
        return redirect("aboutpage")
    return render(request, "home.html")


def about_page(request):
    
    return render(request, "about.html")