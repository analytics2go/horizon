# ----------------------------------------------
# CPSC-442-11/Python  - Assignment 3 Problem 1
# Author:  Wofford, Juana 1014901
# Problem 5
#  You are given a square 2-D array and each value
#  is termed as the height of each building. We can
# increase the height of each building. However, the increase
#  should not exceed the height of the tallest building in
# the same row and column.  Write a function to return a
# new 2-D array that shows the maximum possible heights.
# Also, you need to return the total sum of height changes.
# ---------


# square 2-D array and each value
# is termed as the height of each building
grid1 = [[3,0,8,4]]
grid2 = [[2,4,5,7]]
grid3 = [[9,2,6,3]]
grid4 = [[0,3,1,0]]


total = sum(sum(grid,[]))
print(total)

