#Exercise 11
#Ask the user for a number and determine whether the number is prime or not.

num = int(input("please give me a number\n"))

allnum = list(range(1,num))

print("all numbers below your input: ", allnum,"\n")

divisor=[]

for factor in allnum:
    if num%factor == 0:
        divisor.append(factor)
    else:
        pass

if divisor == [1]:
    print("this word is a prime number")
else:
    print("this word is not a prime number")
    
# Online Solution

num = int(input("please give me a number\n"))
a = [i for i in range(1,num-1) if num%i == 0]

print(a)

if a == [1]:
    print("this word is a prime number")
else:
    print("this word is not a prime number")
    