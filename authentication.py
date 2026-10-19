#Storing the username and password
user = 'whatisamax'
password = "piano123"

import getpass

#Using a while loop to allow the user to enter their username and password until they get it right
Flag = False
#Limiting the number of attempts to 3
maxattempts = 3
while not Flag and maxattempts > 0:
    userinput = str(input("Enter username: "))
    passwordinput = getpass.getpass("Enter password: ")
    if userinput == "" or passwordinput == "":
        print("Username and password cannot be empty. Please try again.")
        continue

    if userinput == user and passwordinput == password:
        print("Login successful")
        Flag = True
    elif userinput != user and passwordinput == password:
        print("Invalid username")
        maxattempts -= 1
    elif userinput == user and passwordinput != password:
        print("Invalid password")
        maxattempts -= 1
    elif userinput != user and passwordinput != password:
        print("Invalid username and password")
        maxattempts -= 1

#Announces when the user has reached the maximum number of attempts
if maxattempts == 0:
    print("Maximum attempts reached. Access denied.") 
