import requests
from bs4 import BeautifulSoup
import re
import time
import csv
import random
#爬取每个网址的分页
fb = open(r'url_1.txt','w')
url = 'http://travel.qunar.com/travelbook/list.htm?page={}&order=hot_heat&avgPrice=1_2'
#请求头，cookies在电脑网页中可以查到
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.360',
         'cookies':'JSESSIONID=5E9DCED322523560401A95B8643B49DF; QN1=00002b80306c204d8c38c41b; QN300=s%3Dbaidu; QN99=2793; QN205=s%3Dbaidu; QN277=s%3Dbaidu; QunarGlobal=10.86.213.148_-3ad026b5_17074636b8f_-44df|1582508935699; QN601=64fd2a8e533e94d422ac3da458ee6e88; _i=RBTKSueZDCmVnmnwlQKbrHgrodMx; QN269=D32536A056A711EA8A2FFA163E642F8B; QN48=6619068f-3a3c-496c-9370-e033bd32cbcc; fid=ae39c42c-66b4-4e2d-880f-fb3f1bfe72d0; QN49=13072299; csrfToken=51sGhnGXCSQTDKWcdAWIeIrhZLG86cka; QN163=0; Hm_lvt_c56a2b5278263aa647778d304009eafc=1582513259,1582529930,1582551099,1582588666; viewdist=298663-1; uld=1-300750-1-1582590496|1-300142-1-1582590426|1-298663-1-1582590281|1-300698-1-1582514815; _vi=6vK5Gry4UmXDT70IFohKyFF8R8Mu0SvtUfxawwaKYRTq9NKud1iKUt8qkTLGH74E80hXLLVOFPYqRGy52OuTFnhpWvBXWEbkOJaDGaX_5L6CnyiQPPOYb2lFVxrJXsVd-W4NGHRzYtRQ5cJmiAbasK8kbNgDDhkJVTC9YrY6Rfi2; viewbook=7562814|7470570|7575429|7470584|7473513; QN267=675454631c32674; Hm_lpvt_c56a2b5278263aa647778d304009eafc=1582591567; QN271=c8712b13-2065-4aa7-a70b-e6156f6fc216',
         'referer':'http://travel.qunar.com/travelbook/list.htm?page=1&order=hot_heat&avgPrice=1'}
count = 1
#共200页
for i in range(1,201):
    url_ = url.format(i)
    try:
        response = requests.get(url=url_,headers = headers)
        response.encoding = 'utf-8'
        html = response.text
        soup = BeautifulSoup(html,'lxml')
        #print(soup)
        all_url = soup.find_all('li',attrs={'class': 'list_item'})
        #print(all_url[0])
        '''
        for i in range(len(all_url)):
            #p = re.compile(r'data-url="/youji/\d+">')
            url = re.findall('data-url="(.*?)"', str(i), re.S)
            #url = re.search(p,str(i))
            print(url)
        '''
        print('正在爬取第%s页' % count)
        for each in all_url:
            each_url = each.find('h2')['data-bookid']
            #print(each_url)
            fb.write(each_url)
            fb.write('\n')
        #last_url = each.find('li', {"class": "list_item last_item"})['data-url']
        #print(last_url)
        time.sleep(random.randint(3,5))
        count+=1
    except Exception as e:
        print(e)