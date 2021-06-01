from django.shortcuts import render
from django.http import HttpResponse
from .models import MyProjects

# Create your views here.
def index(request):
    return render(request, "index.html", {

    })

def results(request):
    return render(request, "results.html", {
        "results": MyProjects.objects.all()
    })