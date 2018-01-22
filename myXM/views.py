# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")
def loginPage(request):
    return render(request,"loginPage.html")
def loginOn(request):
    user=request.POST['user']
    pwd=request.POST['pwd']
    print user,pwd
def capPage(request):
    return render(request,"capPage.html")
def capitalize(request):
    cap=request.POST['cap']
    for x in cap.split():
        print x.capitalize(),
    # print cap.capitalize()