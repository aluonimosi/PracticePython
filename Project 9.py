#==============================================================================
# GuessGame
#==============================================================================
import random

# Game function

def guessnumber():
    
    key = random.randint(1,10)
    guess = int(input("guess the number\n\n"))
    count = 0
    
    while guess!=key:
        if guess>key:
            print("your guess is too high, please try again")
            
        if guess<key:
            print("your guess is too low, please try again")
            
        guess = int(input("guess the number\n\n"))  
        count = count + 1
        
    if guess==key:
        print("you got it!")
        count = count + 1
        print("it only took you", count, "tries!")
        
# to play again or not        
        command = input("do you want to play again? yes/no\n\n")
        if command == 'yes':
            guessnumber()
        if command == 'no':
            print("\nok, byebye")
        else:
            print("\ndon't be a goof")
            command = input("do you want to play again? yes/no\n\n")
            if command == 'no':
                print("\n ok, byebye")
            
guessnumber()     
   
