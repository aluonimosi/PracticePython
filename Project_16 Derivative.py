import random

n1 = random.randint(1,random.randint(1,7))
n2 = random.randint(1,10-n1-2)
n3 = random.randint(1,10-n1-n2-1)
n4 = 10-n1-n2-n3

sumlist = []
unitlist = []
count = 1

while count <=100:
    n1 = random.randint(1,7)
    n2 = random.randint(1,10-n1-2)
    n3 = random.randint(1,10-n1-n2-1)
    n4 = 10-n1-n2-n3
    
    unitlist.append(n1)
    unitlist.append(n2)
    unitlist.append(n3)
    unitlist.append(n4)
    sumlist.append(unitlist)
    unitlist = []
    count += 1
  
print(sumlist)

import csv

with open('output.csv', 'w') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(sumlist)