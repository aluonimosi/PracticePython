# Exercise 16
# Random password generator
# a mix of lowercase letters, uppercase letters, numbers, and symbols

import random

list = []
choicepool1 = ['0','1','2','3','4','5','6','7','8','9']
choicepool2 = ["a","b","c","d","e","f","g","h","i","j","k","l",'m','n','o','r','s','t','u','v','w','x','y','z']
choicepool3 = ["!","@","#","$","%","^","&","*","(",")","_","+","-","=",",",".","/",";"]
choicepool4 = []
               
# To creat capitalized choicepool4
for i in choicepool2:
    choicepool4.append(i.upper()) 

# To decide how many factors to pick from each list

def password_generator():

    n1 = random.randint(1,random.randint(1,7))
    n2 = random.randint(1,10-n1-2)
    n3 = random.randint(1,10-n1-n2-1)
    n4 = 10-n1-n2-n3
    print ("how many factors to pick from choicepool1: ", n1)
    print ("how many factors to pick from choicepool2: ", n2)
    print ("how many factors to pick from choicepool3: ", n3)
    print ("how many factors to pick from choicepool4: ", n4)

# To randomly pick up the factors from each list

    pick1 = random.sample(choicepool1, n1)
    pick2 = random.sample(choicepool2, n2)
    pick3 = random.sample(choicepool3, n3)
    pick4 = random.sample(choicepool4, n4)
    print('the factors picked from choicepool1 are: ', pick1)
    print('the factors picked from choicepool2 are: ', pick2)
    print('the factors picked from choicepool3 are: ', pick3)
    print('the factors picked from choicepool4 are: ', pick4)

    password = []
    for i in pick1:
        password.append(i)
    for i in pick2:
        password.append(i)
    for i in pick3:
        password.append(i)
    for i in pick4:
        password.append(i)

    print('the password factors list is: ',password)

# To shuffle the password list
    random.shuffle(password)

    print('the shuffled password list is: ', password)

# To change a list to a string

    output = "".join(password)
    print('the final password generated is: ', output)
    
password_generator()
