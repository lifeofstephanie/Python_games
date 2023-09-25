import random

choices =  ['rock', 'paper', 'scissors']
while True:
    player_choice = input('Enter rock, paper or scissors: ')
    if player_choice not in choices:
        print('Invalid, try again')
        continue
    computer_choice = random.choice(choices)
    print('Computer choice: '+ computer_choice)
    if player_choice == computer_choice:
        print('It is a tie!')
    elif player_choice == 'rock' and computer_choice == 'scissors':
        print('You win!')
    elif player_choice == 'scissors' and computer_choice == 'paper':
        print('You win!')
    elif player_choice == 'paper' and computer_choice == 'rock':
        print('You win!')
    else:
        print('Computer wins!')