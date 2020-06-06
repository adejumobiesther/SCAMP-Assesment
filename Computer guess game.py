import random
trial = int(input("how many times do you want to retry the guess_game?\n"))
i,result = 0,0
while i<trial:
    computer_number = random.randint(0,20)
    player_guess = int(input("Enter a guess number between 0 and 20\n" ))
    print("correct!"if computer_number == player_guess else "wrong, try harder!")
    result+=1 if computer_number == player_guess else result
    i +=1

print("You got {} guesses out of {} trials".format(result, trial))
