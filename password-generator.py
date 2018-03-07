# !/usr/bin/python
import random, string

# def generate_passwords(password_length,add_special_characters,seed):
#     randomSystem = random.SystemRandom()
#
#
#     seed_lowercase_letters = string.ascii_lowercase
#     seed_uppercase_letters = string.ascii_uppercase
#     seed_numbers = string.digits
#     seed_special_char = string.punctuation
#
#     if(seed == None):
#         if(add_special_characters):
#             pass_seed = seed_lowercase_letters + seed_uppercase_letters + seed_numbers + seed_special_char
#             output_password = str().join(randomSystem.choice(pass_seed) for _ in range(password_length))
#         else:
#             pass_seed = seed_lowercase_letters + seed_uppercase_letters + seed_numbers
#             output_password = str().join(randomSystem.choice(pass_seed) for _ in range(password_length))
#
#     # output_password = str().join(randomSystem.choice(alphabet) for _ in range(password_length))
#     return output_password;


def generate_password(password_length,add_lowerCase,add_upperCase,add_numbers,add_specialChar,seed):
    randomSystem = random.SystemRandom()

    #gets all the characters on a keyboard and puts it in their on category
    seed_lowercase_letters = string.ascii_lowercase
    seed_uppercase_letters = string.ascii_uppercase
    seed_numbers = string.digits
    seed_special_char = string.punctuation

    #this is what the machine randomy chooses
    passChain = ""

    if(seed == None):
        if(add_lowerCase):
            passChain += seed_lowercase_letters
        if(add_upperCase):
            passChain += seed_uppercase_letters
        if(add_numbers):
            passChain += seed_numbers
        if(add_specialChar):
            passChain += seed_special_char
    else:
        passChain = seed



    output_password = str().join(randomSystem.choice(passChain) for _ in range(password_length))
    return output_password


print(generate_password(20,True,True,True,True,None))
