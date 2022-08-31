import random

user_number = 0
computer_number = int(random.randint(1,10))
print(computer_number)
lives = 5
guess = "Wrong"



def turn():
    global lives
    global guess
    print("\nYou have {} lives".format(lives))
    user_number = int(input("Guess my number from 1 - 10: "))
    if user_number > 10 or user_number < 1:
        user_number = int(input("\nFrom 1 - 10 pls: "))
    elif user_number != computer_number:
        print("Wrong guess!\n")
        lives -= 1
        if computer_number < user_number:
            print("Lower")
        else:
            print("HIgher")
    else:
        print("Congrats, you won!")
        guess = "Right"
        
    

    

while guess == "Wrong" and lives > 0:
    turn()


if guess == "Wrong" and lives == 0:
    print("Out of lives")
else:
    print("Game over")
   
    
    
    
    

