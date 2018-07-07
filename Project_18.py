#Exercise 18
# "Cows and Bulls" game
#Logic: 	
# 1. Randomly generate a 4-d number lst1 = [a,b,c,d]
# 2. User input lst2 = [w,x,y,z]
# 3. e.g. if lst1[1] in lst2: it's a bull
    # a. If lst1[1] = lst2[1], it's not a bull, it’s a cow
# 4. Track how many by a counter


import random

randnum = random.sample(range(0,9),4)


def cows_and_bulls():
    key_lst = []
    answer_lst = []
    answer = input("Please guess the four digits \n")
    bull = 0
    cow = 0
    count = 0
    n = 0
    
    for i in randnum:
        key_lst.append(str(i))

    for i in answer:
        answer_lst.append(i)


    for i in answer_lst:
        if i in key_lst:
            bull +=1
        else:
            pass
    
    while n < 4:
        if answer_lst[n] == key_lst[n]:
            cow += 1
            bull -= 1
        else:
            pass
        n += 1

    print('you have ', bull, 'bulls')
    print('you have ', cow, 'cows')
