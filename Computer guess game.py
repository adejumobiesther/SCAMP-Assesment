import random
computer_number = random.randint(0,20)
player_guess = int(input("Enter a guess number between 0 and 20\n" ))
if player_guess < computer_number:
    print("The guess {}, is lower than the actual number by {}".format(player_guess, (computer_number-player_guess)))
elif player_guess > computer_number:
    print("The guess {}, is higher than the actual number by {}".format(player_guess, player_guess-computer_number))
else:
    print("You are a great guesser!")
