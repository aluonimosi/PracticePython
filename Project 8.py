a = input("user1 ")
b = input("user2 ")

def game(a,b):
    
while true:
    
    if a == "rock":
        if b == "scissors":
            print("a wins")
        elif b == "paper":
            print("b wins")
        elif b == "rock":
            print("it's a draw")
        else:
            print("user 2 wrong input")
    elif a == "scissors":
        if b == "rock":
            print('b wins')
        elif b == 'scissors':
            print("it's a draw")
        elif b== 'paper':
            print('a wins')
        else:
            print('user 2 wrong input')
    elif a == 'paper':
        if b == 'rock':
            print('a wins')
        elif b =='scissors':
            print('b wins')
        elif b == 'paper':
            print("it's a draw")
        else:
            print('user 2 ewrong input')
    else:
        print('user 1 wrong input')
        
    usr_command = input ("continue or quit?")
    if user_command =='quit':
        break

game(a,b)