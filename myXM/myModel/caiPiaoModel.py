# coding:utf-8
import os
import xlrd
from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt
def makeMoney(neiRong):
    BASE_DIR=os.path.dirname(os.path.dirname(__file__))
    DIR=os.path.abspath(os.path.join(BASE_DIR,"static/document/x3d.xls"))
    x3dBook=xlrd.open_workbook(DIR)
    x3dData=x3dBook.sheet_by_name("3d")
    ncols=x3dData.ncols
    nrows=x3dData.nrows
    # print ncols,nrows
    li=[]
    for x in range(1,nrows):
        rdata=x3dData.row_values(x)
        new_data = []
        k=""
        for j in rdata[1:]:
            k+=j

        new_data.append(int(k.encode("raw-unicode-escape")))
        li.append(new_data)
    # print li
    X=li[0:-1]
    Y=li[1:]
# ============================数据准备完成===================================
    clf=linear_model.LinearRegression()   #使用线性回归
    clf.fit(X,Y)
    print np.array(int(neiRong)).reshape(-1,1)
    print clf.predict(np.array(int(neiRong)).reshape(-1,1))
    # print clf.predict(int(neiRong))
    jg=clf.predict(int(neiRong))[0][0]
    result=int(jg)
    print result

# ============================
    X2 = X
    Y2 = clf.predict(X2)
    print 1
    plt.figure()
    plt.title(u'mt test')
    plt.xlabel(u'历史',fontproperties="SimHei")
    plt.ylabel(u'new')
    plt.axis([0,1000,0,1000])
    plt.grid(True)
    plt.plot(X,Y,'r.',label="$%s$" % "ycsj")  #绘制训练数据集散点图 xy红色的点
    plt.plot(X2, Y2, 'g--', label="$%s$" % "jgsj")  # 绘制预测数据集直线  绿色的实线
    plt.legend()   #出图
    plt.show()
    print 11111111111111111111


    return ""
if __name__=="__main__":
    makeMoney("213")