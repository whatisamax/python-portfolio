#Storing the username and password
user = 'whatisamax'
password = "piano123"

#Using a while loop to allow the user to enter their username and password until they get it right
Flag = False
maxattempts = 3
while not Flag:
    userinput = str(input("Enter username: "))
    passwordinput = str(input("Enter password: "))
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

    if maxattempts == 0:
        print("Too many failed attempts. Please try again later.")
        break