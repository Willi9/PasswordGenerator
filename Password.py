import string
import random

# Creating a list to generate the characters that we are going to use 
characters = list(string.ascii_uppercase + string.ascii_lowercase + string.digits + "!@#$%,.?")

def passwordGenerator(length):

    #list where the password is going to be stored
    password = []

    #shuffle the characters 
    random.shuffle(characters)

    #Picking random characters from the characters list 
    for i in range(length):
        password.append(random.choice(characters))
    
    # returning the list as a string
    stringPassword = ''.join(password)
    
    return stringPassword



lengthPassword = int(input("Enter the length of the password: "))

finalPassword = passwordGenerator(lengthPassword)

print(finalPassword)

