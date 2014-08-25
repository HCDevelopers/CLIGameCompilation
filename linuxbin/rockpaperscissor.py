import random
from random import choice

user_score = 0
pc_score = 0

usr_choice = ['paper', 'scissor', 'rock']

user_name = input('Please enter your good name: ')

print('Welcome', user_name, '!')

stat = True
while stat:
    print('Welcome to Paper Scissor and Rock Game')

    print('Your Score is: ', user_score)

    print('PC score is: ', pc_score)
    
    print('Choose your pick: Paper, Scissor or Rock')

    usr_pick = input(': ')

    pc_pick = random.choice(usr_choice)

    if pc_pick == 'paper' and usr_pick == 'scissor':
        print('Scissor beats rock', user_name, 'gets the point')
        user_score += 1

    elif pc_pick == 'scissor' and usr_pick == 'paper':
        print('Scissor tears the Paper and PC get the point')
        pc_score += 1

    elif pc_pick == 'scissor' and usr_pick == 'rock':
        print('Rock crushes the Scissor and', user_name, 'takes the point')
        user_score += 1

    elif pc_pick == 'rock' and usr_pick == 'scissor':
        print('Rock destroyes the scissor PC takes the point')
        pc_score += 1

    elif pc_pick == 'rock' and usr_pick == 'paper':
        print('Paper covers the Rock and', user_name, 'takes the point')
        user_score += 1

    elif pc_pick == 'paper' and usr_pick == 'rock':
        print('Paper Dumps the Rock and PC takes the point!')
        pc_score += 1

    elif pc_pick == usr_pick:
        print('Thats a tie, For fun I will deduct points B-) IMA Boss')
        pc_score -= 1
        user_score -= 1
