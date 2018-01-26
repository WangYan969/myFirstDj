# coding:utf-8
from splinter.browser import Browser
from time import sleep
def buyTicket(object):
    def __init__(self,username,password,order,passengers,dtime,starts,ends):
        self.username=username  #用户名
        self.passwd=password    #密码
        self.order=order
        # 乘客名
        self.passengers=passengers
        # 起始地点和终点
        self.starts=starts
        self.ends=ends
        # 日期
        self.dtime=dtime
        self.login_url='https://kyfw.12306.cn/otn/login/init'  #12306登录页
        self.initMy_url='https://kyfw.12306.cn/otn/index/initMy12306'  #登录成功的地址
        self.ticket_url='https://kyfw.12306.cn/otn/leftTicket/init'  #购票的地址
        self.driver_name='chrome'
        self.executable_path=''       #;;;;;;;;;;;;;;;;;;;;;安装位置