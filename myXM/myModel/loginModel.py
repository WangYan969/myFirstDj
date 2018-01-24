# coding:utf-8
from myXM import models

class loginModel(object):
    def loginOn(self,user,pwd):
        try:
            result=models.user.objects.get(userName=user)
            if result.passWord==pwd:
                return 1
            else:
                return 0
        except:
            return -1