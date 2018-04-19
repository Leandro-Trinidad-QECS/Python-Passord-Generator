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
    # this is the variable that the program chooses characters from
    passChain = "" # puts the above variables in here if the user wants to

    #if the user doesnt want to use a seed
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

    # then
    # randomly chooses from the passchain
    output_password = ""
    for i in range(password_length):
        output_password += "".join(randomSystem.choice(passChain))

    return output_password

def checkBool(name):
    # checks if the user has typed in true or false
    max_Try = 0
    while max_Try <= 3:
        user_input = input(name+ " [T/F] ")
        if user_input in ("True","T","true","t"):
            return True
        if user_input in ("False","F","false","f"):
            return False
        else:
            print("try again")
            max_Try +=1
    exit(0)
def checkNum(name):
    # checks if the user input is a number
    max_Try = 0
    while max_Try <= 3:
        try:
            user_input = int(input(name))
            return user_input
        except:
            print("try again")
            max_Try +=1
    exit(0)
        
            
length = checkNum("Password Length ")
lowercase = checkBool("Add Lowercase? ")
uppercase = checkBool("Add UpperCase? ")
numbers = checkBool("Add numbers? ")
specialChar = checkBool("Add special character? ")
seed = str(input("seed "))

print("----------  %s  ----------" % (generate_password(length,lowercase,uppercase,numbers,specialChar,seed)))
