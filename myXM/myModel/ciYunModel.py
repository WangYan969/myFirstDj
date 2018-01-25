# coding:utf-8
from PIL import Image
import numpy as np
import os
from wordcloud import WordCloud,ImageColorGenerator
from os import path
import jieba.analyse
import sys
reload(sys)
sys.setdefaultencoding('utf8')
def makeIt(image,wenBen):
    print 111111111111111111
    tags =jieba.analyse.textrank(wenBen, topK=1000, withWeight=True) #虽然算法不同 但基本内容相似
    print 2222222222222
    keywords={}
    print tags
    for x in tags:
        keywords[x[0]]=x[1]
    print str(keywords).decode("unicode-escape")
    print 33333333333333333
    myImg=Image.open(image)
    graph=np.array(myImg)

    BasePath=os.path.dirname(os.path.dirname(__file__))
    fontPath=os.path.abspath(os.path.join(BasePath,"static/fonts/simhei.ttf"))  #字体路径
    print 1
    wc=WordCloud(font_path=fontPath,background_color='white',max_words=1000,mask=graph)
    wc.generate_from_frequencies(keywords)                #传入词频
    image_color=ImageColorGenerator(graph)             #从背景颜色生成颜色值
    print 2
    wc.recolor(color_func=image_color)         #通过这种方式 词云将会按照给定的图片颜色布局生成字体颜色策略
    wc.to_file(path.join(BasePath,"static/img/wy.jpg"))  #将图片保存起来

    return 1
