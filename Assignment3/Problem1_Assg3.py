# ----------------------------------------------
# CPSC-442-11/Python  - Assignment 3 Problem 1
# Author:  Wofford, Juana 1014901
#
# Program Problems:
# 1. Remove duplicates from a list without the use
# of any loops i.e. for, while or if statements
#  Input: [1,3,2,5,1,3,7,6,2,3]
#  Output: [1, 2, 3, 5, 6, 7]
# -----------------------------------------

# define list called value_list
value_list = [1,3,2,5,1,3,7,6,2,3]

# display the list with duplicates
print('\nInput: {}'.format(value_list))

# use the set function on the list
# sets are like lists but don't allow for duplicates
value_list_nodups = set(value_list)
print('Output: {}'.format(value_list_nodups))
