# CPSC-442-11/Python  - Assignment 1 Problem 1
# Author:  Wofford, Juana 1014901
#
# Program prompts the user for a Celsius temperature
# the program will convert the entered temperature to Fahrenheit
# and display the result
# -----------------------------------------

# Prompt the user to enter a Celsius temperature
print('\n')
celsius = input('Hello, please enter a temperature in Celsius:')

# Display what the user has entered for the Celsius temperature
print('You entered: ', celsius)

# Convert the entered Celsius temperature to Fahrenheit
# and display results
fahrenheit = ((int(celsius) * 9)/ 5 +32)
print(celsius + ' degrees Celsisus is '+str(int(fahrenheit))+ ' degrees fahrenheit')