from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    names = []
    title = "Home page"
    return render(request,"index.html",context={"names" : names,"title":title})

def about(request):
    names = []
    title = "about page"
    return render(request,"about.html",context={"names" : names,"title":title})

def contact(request):
    names = []
    title = "contact page"
    return render(request,"contact.html",context={"names" : names,"title":title})


def success_page(request):
    return HttpResponse("<h1>hii this is a success page</h1>")

