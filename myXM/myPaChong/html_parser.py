# coding:utf-8
from bs4 import BeautifulSoup
import  re
import urlparse
class HtmlParser(object):
    def parpase(self, new_url, html_content):
        soup=BeautifulSoup(html_content,"html.parser",from_encoding="utf-8")
        new_urls=self.get_new_urls(new_url,soup)
        new_data=self.get_new_data(new_url,soup)
        return new_urls,new_data

    def get_new_urls(self, page_url, soup):
        new_urls=set() #定义集合,用于存新urls的
        links=soup.find_all("a",href=re.compile(r"/8hr/page/\d/"))  # 抓"a"标签
        for link in links:
            part_url=link["href"]
            new_full_url = urlparse.urljoin(page_url,part_url)   #拼接成完整的url
            new_urls.add(new_full_url)   #把重复的 过滤掉
        return new_urls

    def get_new_data(self, page_url, soup):
        res_data={}
        res_data["title"]=page_url  #存一下url
        user_node=soup.find("div",class_="author clearfix")  #这里没有找所有 是练习find 查一下 所以每一页面爬一个
        user_name=user_node.find_all("a")[1].find("h2").get_text().strip()
        res_data["userName"]=user_name.encode("utf-8") #存一下用户名
        #抓笑话内容
        joke_content=soup.find("div",class_="content").find("span").get_text().strip()
        res_data["content"]=joke_content.encode("utf-8") #存一下笑话
        return res_data