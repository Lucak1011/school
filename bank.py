# This exercise will test your skills in programming with subroutines
# Program that models the workings of a bank
# Name:

# DON'T TOUCH - This code makes the balance work throughout your program
global accountBalance

# Task 1:   Write a line of code that sets the value of accountBalance to 0.00
accountBalance = 0.00


# Task 2:   Write a subroutine called printWelcome that prints a welcome message to the customer
def printWelcome():
    print("Welcome to the bank of banks")
    print("Below is a function menu. USE IT")
    
    

# Task 3:   Write a subroutine called mainMenu that prints a list of choices for the customer
#           The choices are:
#           1 - Check balance
#           2 - Deposit money
#           3 - Withdraw money
#           9 - Quit
def mainMenu():
  print("Option 1 - check balance")
  print("Option 2 - deposit money")
  print("Option 3 - Withdraw money")
  print("Option 9 - exit")
        


# Task 4:   Write a subroutine called menuChoice that asks the customer to choose a number from the menu
#           The customers choice should be stored in a variable called userMenuChoice
#           The subroutine should use IF, ELSE and ELIF to run the subroutines checkBalance, depositMoney and withdrawMoney depending on the choice they have made
#           If the user enters something that isn't one of the listed numbers, then they are asked to choose again - HINT run the menuChoice function again
def menuChoice():
  opt = int(input("Enter an option"))
  if opt == 1:
    checkBalance()
  elif opt == 2:
    depositMoney()
  elif opt == 3:
    withdrawMoney()


# Task 5:   Write a subroutine called checkBalance that outputs the variable 'accountBalance' of the account
def checkBalance():
    print(accountBalance)



# Task 6:   Add to the subroutine called depositMoney that allows the customer to add money to their balance
#           The program will then output their new balance to confirm the transaction has been completed successfully
def depositMoney():
    global accountBalance
    depam = int(input("Enter an amount to deposit"))
    accountBalance = accountBalance + depam
    

# Task 7:   Add to the subroutine called withdrawMoney that allows the customer to take money from their balance
#           Make sure that they are not allowed to take more money than they have in the balance
#           The program will then output their new balance to confirm the transaction has been completed successfully
def withdrawMoney():
    global accountBalance
    witham = int(input("Enter an amount to withdraw")
    accountBalance = accountBalance - witham
    

# DON'T TOUCH - This code will run your program for you once you have completed the tasks above
printWelcome()
while True:
    mainMenu()
    menuChoice()

# Extension Task:   At the moment, the customer starts with 0.00 each time the program runs. This means they lose their money when the program closes!
#                   Amend the code so that the balance is saved in a text file on the computer. 
#                   When the program opens it should read the balance from the text file so that the customer doesn't start with 0.00 each time the program opens.

