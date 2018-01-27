# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect   #用于重定向
from django.shortcuts import render
from myModel.loginModel import loginModel
from myModel.registerModel import registerModel
from myModel import ciYunModel
from PIL import Image
from os import path
from myModel.ticketModel import buy_ticket_obj
# Create your views here.
from time import sleep
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

def buyTicketPage(request):
    return render(request, "ticketPage.html")


# def buyTicket(request):
#     loginUrl="https://kyfw.12306.cn/otn/login/init"
#     userName="axj5562880"
#     passWord="AXJ5562880"
def buyTicket(request):
    print 12345
    username = 'DynastY'
    password = "wangyan1110"
    # 车次选择， 0 代表所有车次
    order = 0
    #乘客名['XX', 'XXX']
    #学生票须注明['XX(学生)']
    passengers = ['龙雪(学生)']
    # 日期，格式为：'2018-01-26'
    dtime = '2018-02-03'
    # 出发地（需填写cookie值）
    starts = '%u54C8%u5C14%u6EE8%2CHBB'
    # 目的地
    ends = '%u6602%u6EAA%CAAX'
    bt = buy_ticket_obj(username, password, order, passengers, dtime, starts, ends)
    bt.buy_ticket()
    sleep(20)
    return 1






def capPage(request):
    return render(request,"capPage.html")
def capitalize(request):
    cap=request.POST['cap']
    cap_result=request.POST['cap']
    for x in cap.split():
        print x.capitalize(),
    # print cap.capitalize()