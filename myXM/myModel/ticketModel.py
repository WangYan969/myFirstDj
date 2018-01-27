# coding:utf-8
#安装splinter：
#  pip install splinter
# 2. 第二种使用git：
#  git clone git://github.com/cobrateam/splinter.git
#  cd splinter
#  python setup.py install
# 3. 第三种直接下载zip文件
#  https://pypi.python.org/pypi/splinter/   python官网下载
#  cd splinter
#  python setup.py install
# 使用方法
# http://blog.csdn.net/lanchunhui/article/details/50243669 csdn使用案例
# http://splinter.readthedocs.io/en/latest/drivers/chrome.html#using-chrome-webdriver  英文安装网站
# http://splinter.readthedocs.io/en/0.7.3/#getting-started  英文使用网站
# http://blog.csdn.net/windanchaos/article/details/54898354  csdn有人写的api
# 谷歌驱动下载
# 谷歌浏览器版本对应 http://blog.csdn.net/huilan_same/article/details/51896672
from splinter.browser import Browser  #引入splinter的borwser对象
from time import sleep

class buy_ticket_obj(object):
    def __init__(self, username, password, order, passengers, dtime, starts, ends):
        self.username = username # 用户名
        self.passwd = password # 密码
        self.order = order
        # 乘客名
        self.passengers = passengers
        # 起始点 终点
        self.starts = starts
        self.ends = ends
        # 日期
        self.dtime = dtime
        self.login_url = 'https://kyfw.12306.cn/otn/login/init'  # 12306首页
        self.initMy_url = 'https://kyfw.12306.cn/otn/index/initMy12306'  # 登录成功的地址
        self.ticket_url = 'https://kyfw.12306.cn/otn/leftTicket/init'  # 购票的路径
        self.driver_name = 'chrome'
        self.executable_path = 'D:\chromedriver.exe'
    def buy_ticket(self):
        print 1111111
        self.driver= Browser(driver_name=self.driver_name)
        print 22222
        # self.driver.driver.set_window_size(1200, 800)
        print 33333
        self.driver.visit(self.login_url)  # 访问地址栏
        sleep(10)
        print 44444
        self.driver.fill('loginUserDTO.user_name', self.username) # 通过name添加用户名
        self. driver.fill('userDTO.password', self.passwd) # 通过passwd添加
        print "该到输入验证码了...."
        while True:
            if self.driver.url != self.initMy_url:
                sleep(1)
            else:
                break  # 结束后，才会走下面的代码
        print 555555

        # self.login()
        self.driver.visit(self.ticket_url) # 进入买票页面
        print 66666666666
        try:
            print u"购票页面开始..."
            self.driver.cookies.add({"_jc_save_fromStation":self.starts})
            self.driver.cookies.add({"_jc_save_toStation":self.ends})
            self.driver.cookies.add({"_jc_save_toDate":self.dtime})
            self.driver.reload()
            count = 0
            print 7777777777777
            while self.driver.url == self.ticket_url:
                count += 1
                self.driver.find_by_text(u"查询").click()
                print u"循环点击查询....第%s次" % count
                sleep(1)
                 # 要买的票的有无的那个标签的id
                tarVal = self.driver.find_by_id('ZE_0h0000G38208').value
                print tarVal
                if tarVal ==u'有':
                    if self.order != 0:
                        self.driver.find_by_text(u"预订")[self.order - 1].click()
                    else:
                        self.driver.find_by_text(u"预订")[0].click()
                    break
                else:
                    continue
            print 101010101010
            print u"开始预定...."
            sleep(1)
            print u'开始选择用户'
            for user in self.users:
                print 88888888888888
                self.driver.find_by_text(user).click()
            print u"提交订单..."
            # #这里是买票种  1 成人  2 儿童 3 学生 4 残疾  参数是name
            self.driver.find_by_xpath('//select[@id="ticketType_1"]/option[@value="0"]')._element.click()
            sleep(1)
            # # 席座  1硬座   3 硬卧   4软卧   9商务座  O是二等座(是o不是0)  M一等座
            self.driver.find_by_xpath('//select[@id="seatType_1"]/option[@value="1"]')._element.click()
            sleep(1)
            # 提交订单
            print u"提交订单..."
            self.driver.find_by_id('submitOrder_id').click()
            sleep(1.5)
            print u"确认选座..."
            self.driver.find_by_id('qr_submit_id').click()
            print 123456789
            return True

        except:
            print "出错了"
            return False




