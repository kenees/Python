import urllib.request

url = "http://www.baidu.com"
page_info = urllib.request.urlopen(url).read()
page_info = page_info.decode('utf-8')
#print(page_info)


#例如：下载网络图片
import urllib.request
def saveImg(imageURL,fileName):
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10')]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(imageURL,fileName)

#saveImg('http://img2.imgtn.bdimg.com/it/u=1064263267,272845117&fm=26&gp=0.jpg','/Users/eme/PycharmProjects/PythonStudy/爬虫/MM/a.jpg')
#saveImg('http://img.mukewang.com/574669dc0001993606000338-240-135.jpg','/Users/eme/PycharmProjects/PythonStudy/爬虫/MM/b.jpg')

#爬取静态网页数据
#需要调用requests he BeautifulSoup库中的bs4工具
import requests
from bs4 import BeautifulSoup
import os

def getContent(page):
    #定义一个变量url，为需要爬取数据我网页网址
    url = 'https://movie.douban.com/subject/26683723/comments?start='+str(page*20)+'&limit=20&sort=new_score&status=P'
    #获取这个网页的源代码，存放在req中，{}中为不同浏览器的不同User-Agent 针对不同浏览器克自行百度、
    req = requests.get(url,{'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'})

    #生成一个Beautifulsoup对象，用以后边的查找工作
    soup = BeautifulSoup(req.text,'html')
    # print(soup)
    xml = soup.find_all('span',class_='short')
    name = soup.find_all('span',class_='comment-info')
    print(name)
    arr=[]
    for i in range(0,len(name)):
        arr.append(name[i].contents[1].string)

    return xml,arr



def setPage(page):
    num = 0 #定义条数的初始值
    params = []
    string = ''

    for i in range(0,page):
        params.append(getContent(i))

    text = params[0][0]
    name = params[0][1]
    # print(text)
    for i in range(len(text)):
        msg = text[i].string
        if not msg is None:
            num+=1
            string+='第'+str(num)+'条：'+name[i]+'  '+msg+'\n'
    print(string)
    fo = open('html.txt','w',encoding='utf-8')
    fo.write(string)
    fo.close()

setPage(2) #爬取2页