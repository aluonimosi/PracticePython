import requests
from bs4 import BeautifulSoup
import csv

lst = []

url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'lxml')

for a in soup.find_all(class_='content-section'):
    for b in a.find_all("p"):
        b = b.text.strip()
        print(b)
        lst.append(b)

with open('content.csv', 'w', newline='') as thefile:
    wr = csv.writer(thefile)
    wr.writerow(lst)