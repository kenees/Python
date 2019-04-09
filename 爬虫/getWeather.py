
import requests
from bs4 import BeautifulSoup
import json
from pyecharts import Line

def getWeather(s,city):
    r = requests.get('http://www.weather.com.cn/weather1d/'+s+'.shtml#search')
    r.encoding = 'utf-8'
    # print(r.text)

    b = BeautifulSoup(r.text,'html.parser')
    script = b.find_all('script')[3].text
    hour3data =str(script)[15:-1]
    js = json.loads(hour3data)
    print(js['7d'])
    near7day = js['7d']
    # for i in range(len(near7day)):
    #     print(near7day[i])
    #     for j in range(len(near7day[i])):
    #         print(near7day[i][j])
    attr = []
    v1 = []
    for j in range(len(near7day[0])):
        # print(near7day[0][j])
        attr.append(near7day[0][j].split(',')[0])
        v1.append(int(near7day[0][j].split(',')[3][0:-1]))
    print(attr)
    print(v1)
    drawLine(city,attr,v1)

def get_city_code(city = '信阳'):
    try:
        s = requests.get('http://toy1.weather.com.cn/search?cityname='+city+'&callback=success_jsonpCallback&_=1551525878822')
        print(s.text)
        #b = str(s.text)[22:-1]
        left = str(s.text).find(':')
        right = str(s.text).find('~')
        print(str(s.text)[left+2:right])
        getWeather(str(s.text)[left+2:right],city)
    except Exception as e:
        pass


def drawLine(city,attr,v1):
    # attr = ['衬衫','羊毛衫','雪纺衫','裤子','高跟鞋','袜子']
    # v1 = [5,20,36,10,75,90]
    line = Line('折线示例图')
    line.add(city,attr,v1,
             mark_point=['average','max','min'],
             mark_point_symbol='diamond',
             mark_point_textcolor='#40ff27')
    line.render('./line01.html')





city = input('请输入查询地址：')
get_city_code(city)
