# ----------------------------------------------
# CPSC-442-11/Python  - Assignment 3 Problem 1
# Author:  Wofford, Juana 1014901
#
# Program Problem:
# Given a matrix, which needs to be horizontally flipped and inverted.
# Flipping the matrix horizontally means each row is reversed.
# Example, row [ 1 0 0 ] would be flipped to [ 0 0 1 ].
# Then you need to invert the matrix i.e. replace 0 by 1 and 1 by 0.
# Example 1:
# Input: [[1,1,0],[1,0,1],[0,0,0]]
# Output: [[1,0,0],[0,1,0],[1,1,1]]
# Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
#     Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
# -----------------------------------------

# define function
def main():
    starting_string = ['[1,1,0]','[1,0,1]','[0,0,0]']
    print('Input String: ')
    print_list(starting_string)  # print original list
    reverse(starting_string)


def reverse(my_string):
    y = ''
    index = len(my_string)
    while index > 0:
        y += my_string[index-1]
        index = index -1
    print('Reversed String: ')
    print_list(y)


#print('list with duplicate values {}'.format(value_list))

#def invert(my_string):

s = "[1,1,0],[1,0,1],[0,0,0]"
print('split: {}'.format(s.split()))


# funciton to print list
def print_list(o):
    for i in o: print(i, end=' ', flush=True)
    print('\n')






if __name__ == '__main__': main()
