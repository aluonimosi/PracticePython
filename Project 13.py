# Exercise 13
# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them

def Fibonnaci_Generator ():
    num = int(input("How many Fibonnaci number do you want?\n" ))
    fib = []
    count = 2
    
    if num == 1:
        fib = [1]
    else:
        fib = [1, 1]
        while count < num:
            fib.append(int(fib[-1]+int(fib[-2])))
            count +=1
    print(fib)
   
    command = input("Do you want to play again? y/n \n")
    if command == "y":
        Fibonnaci_Generator()
    if command == "y":
        pass
    
Fibonnaci_Generator ()