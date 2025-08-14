from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home_page_view(request):
    return render(request, "pages/home.html")

def about_page_view(request):
    context = {
        "name" : "Mantu",
        "age"  : 30,
    }
    return render(request, "pages/about.html",context)