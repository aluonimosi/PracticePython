import requests
from bs4 import BeautifulSoup

url = 'http://www.nytimes.com/'

r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")

heading_lst = []
unit_lst = []

for story_heading in soup.find_all(class_="story-heading"):
    if story_heading.a:
        story_heading = story_heading.text.strip()
        unit_lst.append(story_heading)
        heading_lst.append(unit_lst)
        unit_lst = []
        print(story_heading)

    else:
        print(story_heading.contents[0].strip())

print(heading_lst)

import csv

with open('header.csv', 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(heading_lst)