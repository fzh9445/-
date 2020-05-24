import requests
from bs4 import BeautifulSoup
import re
import time
import csv
import random

url_list = []
with open('url_1.txt','r') as f:
    for i in f.readlines():
        i = i.strip()
        url_list.append(i)

the_url_list = []
for i in range(len(url_list)):
    url = 'http://travel.qunar.com/youji/'
    the_url = url + str(url_list[i])
    the_url_list.append(the_url)
last_list = []
def spider():
    headers = {
              'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.360',
              'cookies': 'QN1=00002b80306c204d8c38c41b; QN300=s%3Dbaidu; QN99=2793; QN205=s%3Dbaidu; QN277=s%3Dbaidu; QunarGlobal=10.86.213.148_-3ad026b5_17074636b8f_-44df|1582508935699; QN601=64fd2a8e533e94d422ac3da458ee6e88; _i=RBTKSueZDCmVnmnwlQKbrHgrodMx; QN269=D32536A056A711EA8A2FFA163E642F8B; QN48=6619068f-3a3c-496c-9370-e033bd32cbcc; fid=ae39c42c-66b4-4e2d-880f-fb3f1bfe72d0; QN49=13072299; csrfToken=51sGhnGXCSQTDKWcdAWIeIrhZLG86cka; QN163=0; Hm_lvt_c56a2b5278263aa647778d304009eafc=1582513259,1582529930,1582551099,1582588666; viewdist=298663-1; uld=1-300750-1-1582590496|1-300142-1-1582590426|1-298663-1-1582590281|1-300698-1-1582514815; viewbook=7575429|7473513|7470584|7575429|7470570; QN267=67545462d93fcee; _vi=vofWa8tPffFKNx9MM0ASbMfYySr3IenWr5QF22SjnOoPp1MKGe8_-VroXhkC0UNdM0WdUnvQpqebgva9VacpIkJ3f5lUEBz5uyCzG-xVsC-sIV-jEVDWJNDB2vODycKN36DnmUGS5tvy8EEhfq_soX6JF1OEwVFXk2zow0YZQ2Dr; Hm_lpvt_c56a2b5278263aa647778d304009eafc=1582603181; QN271=fc8dd4bc-3fe6-4690-9823-e27d28e9718c',
              'Host': 'travel.qunar.com'
              }
    count = 1
    for i in range(len(the_url_list)):
        try:
            print('正在爬取第%s页'% count)
            response = requests.get(url=the_url_list[i],headers = headers)
            response.encoding = 'utf-8'
            html = response.text
            soup = BeautifulSoup(html,'lxml')
            information = soup.find('p',attrs={'class': 'b_crumb_cont'}).text.strip().replace(' ','')
            info = information.split('>')
            if len(info)>2:
                location = info[1].replace('\xa0','').replace('旅游攻略','')
                introduction = info[2].replace('\xa0','')
            else:
                location = info[0].replace('\xa0','')
                introduction = info[1].replace('\xa0','')
            #print(location)
            #print(introduction)
            other_information = soup.find('ul',attrs={'class': 'foreword_list'})
            when = other_information.find('li',attrs={'class': 'f_item when'})
            time1 = when.find('p',attrs={'class': 'txt'}).text.replace('出发日期','').strip()
            howlong = other_information.find('li',attrs={'class': 'f_item howlong'})
            day = howlong.find('p', attrs={'class': 'txt'}).text.replace('天数','').replace('/','').replace('天','').strip()
            howmuch = other_information.find('li',attrs={'class': 'f_item howmuch'})
            money = howmuch.find('p', attrs={'class': 'txt'}).text.replace('人均费用','').replace('/','').replace('元','').strip()
            who = other_information.find('li',attrs={'class': 'f_item who'})
            people = who.find('p',attrs={'class': 'txt'}).text.replace('人物','').replace('/','').strip()
            how = other_information.find('li',attrs={'class': 'f_item how'})
            play = how.find('p',attrs={'class': 'txt'}).text.replace('玩法','').replace('/','').strip()
            Look = soup.find('span',attrs={'class': 'view_count'}).text.strip()
            if time1:
                Time = time1
            else:
                Time = '-'
            if day:
                Day = day
            else:
                Day = '-'
            if money:
                Money = money
            else:
                Money = '-'
            if people:
                People = people
            else:
                People = '-'
            if play:
                Play = play
            else:
                Play = '-'
            last_list.append([location,introduction,Time,Day,Money,People,Play,Look])
            #设置爬虫时间
            time.sleep(random.randint(2,4))
            count+=1
        except Exception as e :
            print(e)
    #写入csv
    with open('Travel_first.csv', 'a', encoding='utf-8-sig', newline='') as csvFile:
        csv.writer(csvFile).writerow(['地点', '短评', '出发时间', '天数','人均费用','人物','玩法','浏览量'])
        for rows in last_list:
            csv.writer(csvFile).writerow(rows)
if __name__ == '__main__':
    spider()