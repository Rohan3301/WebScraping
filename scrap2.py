import re
import time
import requests
from bs4 import BeautifulSoup

file="hello.html"

state=1

while(state==1):
    #response = requests.get(url)
    content=open(file,"r")
    soup = BeautifulSoup(content,'html.parser')
    mydivs=soup.find_all('div',class_="test")
    #print (mydivs[0])
    strprice=str(mydivs[0]) 
    intprice=int(re.sub(r'[^\w\s]','',strprice[18:24]))
    print(intprice)
    if(intprice<60000):
        print("The price has dropped. Buy now!")
        state=0
    else:
        print("The price is the same, wait till it comes down.")
    time.sleep(2)
