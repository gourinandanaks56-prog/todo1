from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *

def home(request):
    return HttpResponse("Todo App")