#Here is where I import all of the modules I require




#Beginning Introduction of the program
print("Welcome to TaptonPIX Automated Data Packaging Program")
#The location of the question, this will decide what the user wants to do, either run with defaults, edit those defaults or view information
#about the program
user_option = int(input("What do you wish to do today? \n Type 1 to run with defaults \n Type 2 to edit defaults \n Type 3 to view information \n"))

#These are the functions that will store each of the commands to go with the user's response
#Number 1 does the defaults, a simple loading from file of the basic commands
def UsrOpt1():
    print("UsrOpt1")

#Number 2 allows the user to edit any of the options necessary; <insert options here>
def UsrOpt2():
    print("UsrOpt2")

#Number 3 allows the user to view information about the program
def UsrOpt3():
    print("\n")
    print("Here is some Useful Program information")
    print("\n \n Creator Name : Callum \n Creator Contact : groeger@c-e.sg \n Project Github : https://github.com/groegercesg/TaptonPIX \n Project Status : Non-Functional")
    print("\n ")
    print("For all other enquiries please visit : groeger@c-e.sg")
    print("Or see the GitHub page!")

#This is some simple validation for the user input to make sure that they only enter numbers, within the range I desire
try:
    if user_option == 1 or user_option == 2 or user_option == 3:
        print("Input Acceptable \n Proceding...")
    else:
        raise ValueError
except ValueError:
    print("Error \n Only enter the numbers listed")

#This runs the UsrOpt1 function when user_option is equal to 1, it loops it to continue the process
while user_option == 1:
    print("Proceding with User Option 1")
    UsrOpt1()
    #break

#This runs the UsrOpt2 function when user_option is equal to 2, it loops it to continue the process
while user_option == 2:
    print("Proceding with User Option 2")
    UsrOpt2()
    #break

#This runs the UsrOpt3 function when user_option is equal to 3.
while user_option == 3:
    print("Proceding with User Option 3")
    UsrOpt3()
    break
