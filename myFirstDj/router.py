# coding:utf-8
from django.shortcuts import HttpResponse,redirect

def DynamicRouter(request,**kwargs):
    app=kwargs.get('app',None)       #接受APP
    function=kwargs.get('function',None)  #接受function
    print app,function
    try:
        appObj=__import__("%s" % app)  #引入对应的APP
        viewObj=getattr(appObj,"views")  #引入对应的app的视图层
        funObj=getattr(viewObj,function)  # 引入对应视图层文件的方法
        result=funObj(request)  #调用对应的方法
        print "成功"
    except:
       print '失败'
    return result