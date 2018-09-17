# ----------------------------------------------
# CPSC-442-11/Python  - Assignment 3 Problem 7
# Author:  Wofford, Juana 1014901
# Problem 7
# Given an sorted array of integers. Every element appears
# twice except for one element. Write a function to find
# that one element appearing only once in the array.
# Do not use numpy, pandas, dictionary for this question.
# Optional Requirement: Try to write the code for this
# question with minimal number of lines i.e. not more than 3-4 lines.
# ---------------------------------------
"""
Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10
 """
# -------------------------------------------
# for each element in the list, it is
# counted to see number of times the element
# occurs.  if element occurs only 1 time then
# return that element
def appearsOnce(mylist):
    x = set([i for i in mylist if mylist.count(i) == 1])
    return x

# Example1
list1 = [1,1,2,3,3,4,4,8,8]
print('\nPrint the element which appears only once -')
print('\nExample 1:')
print('Input: {}'.format(list1))
answer = appearsOnce(list1)
print('Output: {}'.format(answer))

# Example2
list2 = [3,3,7,7,10,11,11]
print('\nExample 2:')
print('Input: {}'.format(list2))
answer = appearsOnce(list2)
print('Output: {}'.format(answer))

