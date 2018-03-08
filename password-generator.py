# !/usr/bin/python
import random, string


def generate_password(password_length,add_lowerCase,add_upperCase,add_numbers,add_specialChar,seed):
    randomSystem = random.SystemRandom()

    #gets all the characters on a keyboard and puts it in their on variables
    seed_lowercase_letters = string.ascii_lowercase
    seed_uppercase_letters = string.ascii_uppercase
    seed_numbers = string.digits
    seed_special_char = string.punctuation

    #this is what the machine randomy chooses
    passChain = ""

    if(seed == None or seed == ""):
        if(add_lowerCase):
            passChain += seed_lowercase_letters
        if(add_upperCase):
            passChain += seed_uppercase_letters
        if(add_numbers):
            passChain += seed_numbers
        if(add_specialChar):
            passChain += seed_special_char
    else:
        # if you want only certain characters it sets the passChain to the
        # seed that you wanted
        passChain += seed.lower() if add_lowerCase else ""
        passChain += seed.upper() if add_upperCase else ""
        passChain += seed_numbers if add_numbers else ""
        passChain += seed_special_char if add_specialChar else ""

        # if (not add_lowerCase or not add_upperCase or not add_numbers or not add_specialChar) else ""



    # randomly chooses from the passchain
    output_password = str().join(randomSystem.choice(passChain) for _ in range(password_length))
    return output_password

# Pass Length, LowerCae?,  UpperCase?, Numbers?, Special Char?, seed
print(generate_password(7,False,False,False,False,"Leo"))
