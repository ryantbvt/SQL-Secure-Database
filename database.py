# import sqlite3
import random

# password
PASSWORD = 'password'

pass_input = input('What is your password?\n')

# while the input isn't the password, ask again

# counter variable to prevent brute force (3 tries)
i = 0
while pass_input != PASSWORD:
    print('Wrong password, try again')
    pass_input = input('What is your password?\n')
    i = i + 1
    print(i)

    if i == 3:
        break
    print('You have incorrectly typed the wrong password 3 times')
    # This is for future, can't actually reset password yet
    print('Please reset your password and try again')

# send email for 2-factor auth
def twoFactor():
    ranNum = random.randint(1000, 9999)
    print(ranNum)

    # setup email

# if 2-factor auth is incorrect, deny access

# if 2-factor auth is correct open database