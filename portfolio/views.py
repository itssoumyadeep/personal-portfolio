from django.shortcuts import render
from django.http import HttpResponse
#import random
# Create your views here.
from .models import Project

def home(request):
    projects = Project.objects.all()
    return render(request,'portfolio/home.html',{'projects':projects})
