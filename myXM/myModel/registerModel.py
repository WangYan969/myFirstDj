# coding:utf-8
from myXM import models
import uuid

class registerModel(object):
    def registerOn(self,user,pwd):
        try:
            models.user.objects.create(id=uuid.uuid4(),userName=user,passWord=pwd)
            return 1
        except:
            return -1