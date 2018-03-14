# !/usr/bin/python
import random, string,math
import time


def generate_password(password_length,add_lowerCase,add_upperCase,add_numbers,add_specialChar,seed):
# The main function that does the generating of the passwords

    # puts system random to a variable
    randomSystem = random.SystemRandom()

    #gets all the characters on a keyboard and puts it in their on variables
    seed_lowercase_letters = string.ascii_lowercase  # abcdefghijklmnopqrstuvwxyz
    seed_uppercase_letters = string.ascii_uppercase  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    seed_numbers = string.digits                     # 0123456789
    seed_special_char = string.punctuation           # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

    # sets up passChain
    passChain = "" # puts the above variables in here if the user wants to

    #if the user doesnt want o use a seed
    if(seed == None or seed == ""):

        # if the options like lowercase is chosen then it adds lowercaseto the seed
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


    # randomly chooses from the passchain
    # the code underneath had a code that i copied on the internet but I changed it to make it my own
    #                was str().join edited to: "".join
    output_password = "".join(randomSystem.choice(passChain) for _ in range(password_length))
    return output_password


# Pass Length, LowerCae?,  UpperCase?, Numbers?, Special Char?, seed
print("----------  %s  ----------" % (generate_password(10,True,True,True,False,None)))
