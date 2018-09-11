# -*- coding:utf-8 -*-
# Python 3.6.6
# 魏然
# InfoGet
# http://qiaotudesign.cn
# 作用于抓取天河学院新闻中心板块目录（手动输入网址版本）

from bs4 import BeautifulSoup
import urllib.request
import os

def appendStrToFile(filePath, string):
    """
    将字符串追加写入文件中
    param filePath: 文件路径
    param string  : 字符串str
    """
    with open(filePath, "ab") as f:
        f.write(string)

def OutInfoLists():
    
    keyword = input('请输入网页地址:')
    html_doc = keyword
    req = urllib.request.Request(html_doc)
    webpage = urllib.request.urlopen(req)
    html = webpage.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    
    appendStrToFile('index.html','<html>\n<body>\n'.encode('GBK')) # 追加 HTML 头
    
    # 遍历并抓取所有标签为li且id为line_u4_? 的所有内容
    for MyNum in range(0, 20): # 可显示的目录行数
     txt_src = soup.find('li',{'id': 'line_u4_'+ str(MyNum)})
     txt = txt_src
     print(txt.get_text())  # 抓取文本
     
     appendStrToFile('index.html', txt.encode('GBK') + "\n".encode('GBK'))
     
def InfoAdds():
    
    appendStrToFile('index.html', '</body>\n</html>\n'.encode('GBK') + "\n".encode('GBK')) # 追加 HTML 尾
    
    lines = open('index.html').readlines() #打开文件，读入每一行
    fp = open('index.html','w') #把数据更新到相同文件中

    if not os.path.exists('index.html'): # 看一下这个文件是否存在
     exit(-1) # 不存在就退出
     
    for s in lines:
     fp.write( s.replace('../../info/','http://thxy.cn/info/').replace('yes','no')) # 修改访问地址 replace是替换，write是写入
    fp.close() # 关闭文件


    lines = open('index.html').readlines() #打开文件，读入每一行
    fp = open('index.html','w') #把数据更新到相同文件中

    if not os.path.exists('index.html'): # 看一下这个文件是否存在
     exit(-1) # 不存在就退出
     
    for s in lines:
     fp.write( s.replace('../info/','http://thxy.cn/info/').replace('yes','no')) # 修改访问地址 replace是替换，write是写入
    fp.close() # 关闭文件

    lines = open('index.html').readlines() #打开文件，读入每一行
    fp = open('index.html','w') #把数据更新到相同文件中

    if not os.path.exists('index.html'): # 看一下这个文件是否存在
     exit(-1) # 不存在就退出
     
    for s in lines:
     fp.write( s.replace('display:none','display:').replace('yes','no')) # 修改列表项显示属性
    fp.close() # 关闭文件
    
while(1):

  OutInfoLists() #函数调用
  InfoAdds() #函数调用 
