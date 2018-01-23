# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect   #用于重定向
from django.shortcuts import render
from myModel.loginModel import loginModel
from myModel.registerModel import registerModel
# Create your views here.

def index(request):
    return render(request,"index.html")
def loginPage(request):
    return render(request,"loginPage.html")
def loginOn(request):
    user=request.POST['user']
    pwd=request.POST['pwd']
    lgM=loginModel()
    result=lgM.loginOn(user,pwd)
    if result==1:
        return HttpResponseRedirect("/")
    else:
        return render(request,"error.html")


def registerPage(request):
    return render(request,"registerPage.html")
def registerOn(request):
    # print 123
    user = request.POST['user']
    pwd = request.POST['pwd']
    rgM=registerModel()
    result=rgM.registerOn(user,pwd)
    return HttpResponseRedirect("/")













def capPage(request):
    return render(request,"capPage.html")
def capitalize(request):
    cap=request.POST['cap']
    for x in cap.split():
        print x.capitalize(),
    # print cap.capitalize()