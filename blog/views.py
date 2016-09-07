#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .models import MySite
# Create your views here.

def home(request):
    posts = MySite.objects.all()
    return HttpResponse("home")

def archives(request):
    return HttpResponse("archives")