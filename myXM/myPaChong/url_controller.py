# coding:utf-8

class UrlControl(object):
    def __init__(self):
        self.new_urls=set()
        self.old_urls=set()

    def add_new_url(self,root_url):        #添加新的url到new_urls中
        if root_url not in self.new_urls and root_url not in self.old_urls: #如果url不在new和old里,添加到new里
          self.new_urls.add(root_url)

    def has_new_url(self):
        return self.new_urls.__len__()>0           #如果new_url的长度大于0 返回True 否则 返回 False

    def get_new_url(self):
        new_url=self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def add_new_urls(self, new_urls):
        for url in new_urls:
            self.add_new_url(url)