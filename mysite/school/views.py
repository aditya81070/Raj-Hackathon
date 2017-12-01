from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import School_details
# Create your views here.

def school_details(request):
    return HttpResponse("<h1>School details</h1>")
