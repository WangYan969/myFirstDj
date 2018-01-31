# coding:utf-8
import html_downloader
import html_outputer
import html_parser
import url_controller

class Spider_man(object):
    def __init__(self):
        self.urls=url_controller.UrlControl()
        self.downloder=html_downloader.HtmlDownloader()
        self.parser=html_parser.HtmlParser()
        self.outputer=html_outputer.HtmlOutputer()
    def pa(self,root_url):
        self.urls.add_new_url(root_url)
        count = 1
        while self.urls.has_new_url():   #给url一个限制,免得他无限循环
            new_url=self.urls.get_new_url()
            print "第{0[0]}个,地址是{0[1]}".format([count,new_url])
            html_content=self.downloder.download(new_url)
            print html_content