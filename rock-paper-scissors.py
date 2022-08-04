import random

def game(choice):
    x = random.choice(('rock','paper','scissors'))
    if x == choice:
        return print('Its a draw')
    elif x == 'rock':
        if choice == 'scissors':
            print(f'I won, my {x} beat your {choice}')
        elif choice == 'paper':
            print(f'You won, your {choice} beat my {x}')
    elif x == 'paper':
        if choice == 'rock':
            print(f'I won, my {x} beat your {choice}')
        elif choice == 'scissors':
            print(f'You won, your {choice} beat my {x}')
    elif x == 'scissors':
        if choice == 'paper':
            print(f'I won, my {x} beat your {choice}')
        elif choice == 'rock':
            print(f'You won, your {choice} beat my {x}')
    

def pick():
    choice = input('Please pick rock, paper or scissors:\n')
    if choice == 'rock' or choice == 'paper' or choice =='scissors':
        game(choice)
    else: pick()

pick()