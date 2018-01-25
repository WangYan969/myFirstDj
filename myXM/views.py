# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect   #用于重定向
from django.shortcuts import render
from myModel.loginModel import loginModel
from myModel.registerModel import registerModel
from myModel import ciYunModel
from PIL import Image
from os import path
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
        return HttpResponseRedirect("/myXM/mainPage/")
    else:
        return render(request,"error.html")


def registerPage(request):
    return render(request,"registerPage.html")

def registerOn(request):
    user = request.POST['user']
    pwd = request.POST['pwd']
    rgM=registerModel()
    result=rgM.registerOn(user,pwd)
    print user,pwd
    return HttpResponseRedirect("/myXM/")

def mainPage(request):
    return render(request,"mainPage.html")

def ciYunPage(request):
    return render(request,"ciYunPage.html")

def makeCiYun(request):
    wenBen=request.POST["wenBen"]
    tuPian=request.FILES['tuPian']
    result=ciYunModel.makeIt(tuPian,wenBen)
    img=Image.open(tuPian)
    savePath= path.join(path.dirname(__file__),"static/img/yuan.jpg")
    img.save(savePath)
    return HttpResponseRedirect("/myXM/ciYunPage")













def capPage(request):
    return render(request,"capPage.html")
def capitalize(request):
    cap=request.POST['cap']
    cap_result=request.POST['cap']
    for x in cap.split():
        print x.capitalize(),
    # print cap.capitalize()