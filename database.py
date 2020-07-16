import sqlite3

# password
PASSWORD = 'password'

pass_input = input('What is your password?\n')

# while the input isn't the password, ask again
while pass_input != PASSWORD:
    # counter variable to prevent brute force (3 tries)
    i = 0
    i = i + 1
    print('Wrong password, try again')
    pass_input = input('What is your password?\n')

    if i == 3:
        break

# send email for 2-factor auth

# if 2-factor auth is incorrect, deny access

# if 2-factor auth is correct open database