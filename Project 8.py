#==============================================================================
# My solution
#==============================================================================

def game(a,b):
    
    while True:
    
        a = input("user1 ")
        b = input("user2 ")

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
        
        usr_command = input ("continue or quit? ")
        if usr_command =='quit':
            break

game(a,b)

#==============================================================================
# Other Solution
#==============================================================================

p_1 = input("What is Player1's request?\n\n").lower()
p_2 = input("What is Player2's request?\n\n").lower()

choices = list(['paper', 'rock', 'scissors'])

if p_1 not in choices:
    print('you are a goof')
if p_2 not in choices:
    print('you are a goof')
    
if p_1 == p_2:
    print("it's a draw")

elif choices.index(p_1)==(choices.index(p_2)+1) % 3:
    print("Player 2 Wins")
elif choices.index(p_1)==(choices.index(p_2)-1) % 3:
    print("Player 1 Wins")
elif choices.index(p_1)==(choices.index(p_2)+2) % 3:
    print("Player 1 Wins")
