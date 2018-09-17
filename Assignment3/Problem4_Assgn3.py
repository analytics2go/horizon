# ----------------------------------------------
# CPSC-442-11/Python  - Assignment 3 Problem 4
# Author:  Wofford, Juana 1014901
# Program Problem 4 write a function for this task
# to return a list of uncommon words
# -----------------------------------------------
# find the words that are not like
# the other string
def notLikeTheOther(str1, str2):
    w = {}    # declare list, w to hold words from the string
    # split returns a list of all the words in the string
    for s in str1.split():
        w[s] = w.get(s, 0) + 1
    for s in str2.split():
        w[s] = w.get(s, 0) + 1
    # return the words assigned to s that are
    # appear exactly once in one of the strings and does
    # not appear in the other string
    return[s for s in w if w[s] == 1]
print('\n')
print('Print the word that is uncommon in two strings-')
# Example 1
print('Example 1: ')
A = 'this apple is sweet'
B = 'this apple is sour'

answer = notLikeTheOther(A, B)
print('Input: A."{}" , B."{}"'.format(A, B))
print('Output: {}'.format(answer))
print('\n')

# Example 2
print('Example 2: ')
A = 'apple apple'
B = 'banana'
answer = notLikeTheOther(A,B)
print('Input: A."{}" , B."{}"'.format(A, B))
print('Output: {}'.format(answer))
print('\n')




