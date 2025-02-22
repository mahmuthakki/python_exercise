import guessing_game

user_guess= int(input("Guess a number:\n")) # Gets an input from user and convert it to an intiger

number= guessing_game.guessing_game() # Generates a random number using guessing_game function

while user_guess!= number:
# This loop, wants user to cahange its input according to the number user guessed and the number random funciton generated.    
    if user_guess < number:
        user_guess= int(input("Too low\n"))
    else:
        user_guess= int(input("Too High\n"))
input("You have found it. The number was {} ".format(number))            
