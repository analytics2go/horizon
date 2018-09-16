# CPSC-442-11/Python  - Assignment 2 Problem 2
# Author:  Wofford, Juana 1014901
#
# This program prompts the user for an integer variable which is used as Year
# A function verifies whether the integer is a leap year or not.
# The function returns True if year entered is a Leap Year an False if year entered is not a leap year
# -----------------------------------------
# Prompt the user to enter a year
# Display what the user has entered for the
print('\n This program will determine if the Year entered is a Leap Year.')
year = input('\n Please Enter a 4 Digit Year value: ')
# print('\nYou entered: ' + year)
print('Input: ' + year)   # print out the value entered by user

# Perform check on number entered
# Check to see if year can be evenly divided by 4, if it can then year is leap year
# check to see if there is a remainder if not do next check
# unless: the year can be evenly divided by 100, it is NOT a leap year, unless:
# the year is also evenly divisible by 400.
#  (using the % modulus  - remainder of the division of left operand by the right)
year = int(year)   # convert the text entered to integer
if year % 4 == 0:
    if year % 100 == 0:

        if year % 400 == 0:
            print('Output: True')
        else:
            print('Output: False')
    else:
        print('Output: True')
else:
    print('Output: False')