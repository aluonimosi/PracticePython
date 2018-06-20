#my solution

import random

a = random.sample(range(1,100),10)
b = random.sample(range(1,100), 10)

print("list_a is ", a)
print("list_b is ", b)

unique_a = []
unique_b = []

for elementa in a:
    if elementa in unique_a:
        pass
    else:
        unique_a.append(elementa)

print ("unique_a list is ", unique_a)

for elementb in b:
    if elementb in unique_b:
        pass
    else:
        unique_b.append(elementb)

print ('unique_ b list is ', unique_b)

newlist = []


for elementa in unique_a:
    if elementa in unique_b:
        newlist.append(elementa)
    else:
        pass
print ('the new list is ', newlist)

#GitHub solution

import random
a = random.sample(range(1,30),15)
b = random.sample(range(1,30),15)
print(a)
print(b)

newlist = []
for i in a:
    if i in b:
        if i in newlist:
            print("duplicates are ", i)
        else:
            newlist.append(i)

print(newlist)
