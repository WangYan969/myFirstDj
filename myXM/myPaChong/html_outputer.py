# coding:utf-8
class HtmlOutputer(object):
    def __init__(self):
        self.datas=[]
    def collect_data(self, new_data):
        self.datas.append(new_data)