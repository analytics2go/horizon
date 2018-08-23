# CPSC-442-11/Python
# Assignment 01
# Program prompts the user for a Celsius temperature
# the program will convert the entered temperature to Fahrenheit
# and display the result
#

celsius = input('Hello, please enter a temperature in Celsius:')
print('You entered: ', celsius)
fahrenheit = ((int(celsius) * 9)/ 5 +32)
print(fahrenheit)
print(celsius + ' degrees Celsisus is '+str(int(fahrenheit))+ ' degrees fahrenheit')