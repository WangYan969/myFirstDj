# coding:utf-8
from myXM import models

class registerModel(object):
    def registerOn(self,user,pwd):
        try:
            # myxm_user1=user(userName=user,passWord=pwd)
            # myxm_user1.save()
            # print result.passWord
            models.user.objects.create(userName=user,passWord=pwd)
            print 22222222
        except:
            return -1