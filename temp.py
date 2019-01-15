

import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://www.naver.com"

req = requests.get(url)
html = req.text

soup = BeautifulSoup(html, 'html.parser')
templist=soup.select('div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li')

a = []

for temp in templist :
    a.append(temp.text)

ranklist =[]
num=1
for i in a:
    if num>9:
        ranklist.append(i[5:-2])
    else:
        ranklist.append(i[4:-2])
    num +=1

for s, list in enumerate(ranklist):
    print(str(s+1) + "위 "+ list)


   


