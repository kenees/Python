'''
    练习爬取起点
'''
import requests
from bs4 import BeautifulSoup


def getMenu(url):
    # url="https://www.81xzw.com/book/110171/"
    req = requests.get(url)

    bs4 = BeautifulSoup(req.text,'html.parser')

    oul = bs4.findChildren('div',class_="mulu")[1].find_all("ul")[0].find_all("li")
    # print(oul)
    arr = []
    for i in range(len(oul)):
        # print(oul[i].contents[0].string)
        arr.append(oul[i].contents[0].string)

    return arr
