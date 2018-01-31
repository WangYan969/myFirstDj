# coding:utf-8
import urllib2
class HtmlDownloader(object):
    def download(self, new_url):
        user_agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36"
        headers={"User-Agent":user_agent}
        req_timeout=5
        request=urllib2.Request(new_url,headers=headers)
        response=urllib2.urlopen(request,None,req_timeout) #这里有一个返回值 是我们的响应
        print response.getcode()
        # 我们判断如果不是200就返回None 否则就如数据就行了
        if response.getcode() != 200:
            return None
        # 从响应中读取页面数据
        return response.read()
    # 这里下载完成 该进行解析 所以去写htmi的parser