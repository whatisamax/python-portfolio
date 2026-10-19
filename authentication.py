#Storing the username and password
user = 'whatisamax'
password = "04aug2009"
#Imports the datetime module to get the current date and time
import datetime
#Hides the password input from the user using the getpass module
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
        #Stores date and time logged and outputs it
        now = datetime.datetime.now()
        print(now.strftime("%Y-%m-%d %H:%M:%S"))
        continue

    if userinput == user and passwordinput == password:
        print("Login successful")
        now = datetime.datetime.now()
        print(now.strftime("%Y-%m-%d %H:%M:%S"))
        print("[INFO] User logged in successfully.")
        Flag = True
    elif userinput != user and passwordinput == password:
        print("Invalid username")
        now = datetime.datetime.now()
        print(now.strftime("%Y-%m-%d %H:%M:%S"))
        print("[WARNING] Invalid username attempt.")
        maxattempts -= 1
    elif userinput == user and passwordinput != password:
        print("Invalid password")
        now = datetime.datetime.now()
        print(now.strftime("%Y-%m-%d %H:%M:%S"))
        print("[WARNING] Invalid password attempt.")
        maxattempts -= 1
    elif userinput != user and passwordinput != password:
        print("Invalid username and password")
        now = datetime.datetime.now()
        print(now.strftime("%Y-%m-%d %H:%M:%S"))
        print("[WARNING] Invalid username and password attempt.")
        maxattempts -= 1

#Announces when the user has reached the maximum number of attempts
if maxattempts == 0:
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
    print("[CRITICAL] Maximum login attempts reached. Access denied.")
