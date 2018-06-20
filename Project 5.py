a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

unique_a = []
unique_b = []

for elementa in a:
    if elementa in newa:
        pass
    else:
        newa.append(elementa)

print ("the unique_a list is ", newa)

for elementb in b:
    if elementb in newb:
        pass
    else:
        newb.append(elementb)

print ('the unique_b list is ', newb)

newlist = []


for elementa in newa:
    if elementa in newb:
        newlist.append(elementa)
    else:
        pass
print ('the new list is ', newlist)