number = int(123)

numberlist= list(range(1, number+1))

divisorlist=[]

for factor in numberlist:
    if number%factor == 0:
        divisorlist.append(factor)
        
print (divisorlist)