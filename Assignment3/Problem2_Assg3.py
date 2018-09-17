# ----------------------------------------------
# CPSC-442-11/Python  - Assignment 3 Problem 2
# Author:  Wofford, Juana 1014901
# Program Problem:
# Given a matrix, which needs to be horizontally flipped and inverted.
# Flipping the matrix horizontally means each row is reversed.
# Example, row [ 1 0 0 ] would be flipped to [ 0 0 1 ].
# Then you need to invert the matrix i.e. replace 0 by 1 and 1 by 0.
# -----------------------------------------
# call functions to reverse string and print
def main():
    starting_string = ['[1,1,0]','[1,0,1]','[0,0,0]']
    print('Input String: ')
    print_list(starting_string)  # print original list
    reverse(starting_string)
#   invert(starting_string)

def reverse(my_string):
    y = ''
    index = len(my_string)  # assigne lenght of string to index
    while index > 0:
        y += my_string[index-1]
        index = index -1          # reverse the string
    print('\nReversed String: ')
    print_list(y)

def invert(my_string):
    inverted =''.join(reversed(my_string))
    for x in inverted:
        if x == '1':    # change the 1 to zeros
            print('....needed more time to understand how todo')

def print_list(o):
    for i in o: print(i, end=' ', flush=True)    # print list

if __name__ == '__main__': main()
