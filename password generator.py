import string
import random
def password_generator():
    password_length = int(input("what should be the length of your password?\n"))
    if password_length < 6:
        raise ValueError("The password should be a minimum of 6 characters long!")
    number_count = int(input("how many numbers, should the password contain?\n"))
    letter_count = int(input("how many letters, should the password contain?\n"))
    numbers = string.digits + string.punctuation
    letters = string.ascii_letters
    password = random.sample(letters, k = letter_count) + random.sample(numbers, k = number_count)
    return " ".join(password)

print(password_generator())

