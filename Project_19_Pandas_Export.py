import requests
from bs4 import BeautifulSoup
import pandas as pd

lst = []

url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'lxml')

for a in soup.find_all(class_='content-section'):
    for b in a.find_all("p"):
        lst.append(b.text)

dataframe = pd.DataFrame({'sentence': lst})

dataframe.to_csv('Project_19_Pandas_Export.csv', index = False, sep = ',')