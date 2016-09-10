#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage

from .models import MySite
# Create your views here.

def home(request):
    posts = MySite.objects.all()
    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage :
        post_list = paginator.page(paginator.num_pages)

    return render(request,'home.html',{'post_list':post_list})



def archives(request):
    return HttpResponse("archives")

def sites(request):
    return HttpResponse("sites")
def aboutme(request):
    return HttpResponse("aboutme")