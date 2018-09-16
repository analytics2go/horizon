# ----------------------------------------------
# CPSC-442-11/Python  - Assignment 3 Problem 1
# Author:  Wofford, Juana 1014901
#
# Program Problem
# -----------------------------------------------

# find the words that are not like
# the other string
def notLikeTheOther(str1, str2):
    # declare list, w to hold words from the string
    w = {}
    # split returns a list of all the words in the string
    # for each word in string A and B will be assigned to s
    for s in str1.split():
        w[s] = w.get(s, 0) + 1
    for s in str2.split():
        w[s] = w.get(s, 0) + 1
    # return the words assigned to s that are
    # appear exactly once in one of the strings and does
    # not appear in the other string
    return[s for s in w if w[s] == 1]

# Example 1
A = 'this apple is sweet'
B = 'this apple is sour'
print('\n')
answer = notLikeTheOther(A,B)
print('Input: {} {}'.format(A,B))
print('Output: {}'.format(answer))
print('\n')

# Example 2
A = 'apple apple'
B = 'banana'
answer = notLikeTheOther(A,B)
print('Input: {} {}'.format(A,B))
print('Output: {}'.format(answer))
print('\n')




