# ----------------------------------------------
# CPSC-442-11/Python  - Assignment 4 Problem 1
# Author:  Wofford, Juana 1014901
#
# Program Problems:
# function to print valid phone numbers. You need to accept
# inputs and output the valid phone numbers on the console
# Format for valid phone numbers is:
# (xxx) xxx-xxxx
# xxx-xxx-xxxx
# where x would be a number.
# ---------------------------------




userInput = 0
while True:
  try:
     userInput = int(input("Enter numbers, area code and phone: "))
  except ValueError:
     print("You did not enter numbers, try again please.")
     continue
  else:
     print('ok')
     break
