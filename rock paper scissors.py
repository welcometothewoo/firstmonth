import random
import time

possible_choices = ['ROCK', 'PAPER', 'SCISSORS']
wins = 0
losses = 0

def turn():
    global possible_choices, wins, losses
    user_input = input('\nYour turn: ')
    computer_choice = random.choice(possible_choices)
    user_choice = user_input.upper()

    
    
    if user_choice in possible_choices:
        if user_choice == 'ROCK' and computer_choice == 'SCISSORS' or user_choice == 'PAPER' and computer_choice == 'ROCK' or user_choice == 'SCISSORS' and computer_choice == 'PAPER':
            print("\nThe computer played...")
            time.sleep(2)
            print(computer_choice)
            time.sleep(0.4)
            wins += 1
            print("\nYou won!\n{} wins\n{} losses\n".format(wins, losses))
            turn()
        elif computer_choice == 'ROCK' and user_choice == 'SCISSORS' or computer_choice == 'PAPER' and user_choice == 'ROCK' or computer_choice == 'SCISSORS' and user_choice == 'PAPER':
            print("\nThe computer played...\n")
            time.sleep(2)
            print(computer_choice)
            losses += 1
            time.sleep(0.4)
            print("\nYou lost :(\n{} wins\n{} losses\n".format(wins, losses))
            turn()
        else:
            print("\nThe computer played...")
            time.sleep(2)
            print(computer_choice)
            time.sleep(0.4)
            print("\nIt was a draw")
            turn()
    else:
        print("Can only enter rock, paper or scissors\n")
        time.sleep(1)
        turn()

            
turn()
