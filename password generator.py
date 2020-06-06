import string
import random
def password_generator():
    number_count = int(input("How many numbers, should the password contain?\n"))
    letter_count = int(input("How many letters, should the password contain?\n"))
    numbers = string.digits + string.punctuation
    letters = string.ascii_letters
    pass_word = " ".join(random.sample(letters, k = letter_count) + random.sample(numbers, k = number_count))
    if len(pass_word)< 6:
        raise ValueError("The password should be a minimum of 6 characters long!")
    return pass_word

print(password_generator())

