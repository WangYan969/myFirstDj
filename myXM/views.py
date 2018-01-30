# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect   #用于重定向
from django.http import HttpResponse
from django.shortcuts import render
from myModel.loginModel import loginModel
from myModel.registerModel import registerModel
from myModel import ciYunModel
from PIL import Image
from os import path
from myModel.ticketModel import buy_ticket_obj
from myModel import caiPiaoModel
import json
import urllib2
import urllib
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
    passengers = ['王岩(学生)']
    # 日期，格式为：'2018-01-26'
    dtime = '2018-01-28'
    # 出发地（需填写cookie值）
    starts = '%u54C8%u5C14%u6EE8%2CHBB'
    # 目的地
    ends = '%u5317%u4EAC%2CBJP'
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

def futureMoneyPage(request):
    return render(request,"futureMoneyPage.html")
def futureMoney(request):
    fm=request.POST['neiRong']
    # print fm
    result,luJing=caiPiaoModel.makeMoney(fm)
    content={}
    content["jieGuo"]=result
    content["luJing"]=luJing
    content_json=json.dumps(content)
    return HttpResponse(content_json,content_type="application/json")
def robotPage(request):
    return render(request,"robotPage.html")
def robot(request):
    neirong=request.POST['neirong'].encode("utf-8")
    API_KEY="ff13b2b9bfd14666afccc234b7ad674e"
    raw_TULINURL="http://www.tuling123.com/openapi/api?key=%s&info=%s" % (API_KEY,neirong)
    send_content={}
    send_content["key"]=API_KEY
    send_content["info"]=neirong
    send_content["userid"]='1112'
    data=urllib.urlencode(send_content)   #适合urllib对数据进行格式化编码
    req = urllib2.Request(url=raw_TULINURL)
    result = urllib2.urlopen(req).read()
    return HttpResponse(result)