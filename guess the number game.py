'''
change the number guessed range 1 to 1,000,000
game would ask us to guess a number
give a clue if the number is higher or lower than given number
inform the player if he/she won
'''
from random import randint
start = 1
end = 1000
value = randint(start, end)
print("A number has been chosen between", start, "and", end)
guess=None
while guess != value:
    text= input("Guess the number: ")
    guess=int(text)
    if guess<value:
        print("The number is higher")
    elif guess >value:
        print("Number is lower")
print("Congratulations you won!!!")