# import sys
# sys.path.append(r'/Users/eme/PycharmProjects/PythonStudy/爬虫/getMenu')

import requests
from bs4 import BeautifulSoup
print(11)
import getMenu.getMenu11


url="https://www.81xzw.com/xuanhuan/"
headers = {

}
req = requests.get(url)

bs4 = BeautifulSoup(req.text,'html.parser')

dd = bs4.find_all('dd')

arrList = []

for i in range(len(dd)):
    print(dd[i].contents[0].text)
    arrList.append(dd[i].contents[0].find('a')['href'])
    text = getMenu.getMenu11.getMenu('https://www.81xzw.com'+dd[i].contents[0].find('a')['href'])
    print(text)

#print(arrList)
#print(dd)

