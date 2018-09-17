# ----------------------------------------------
# CPSC-442-11/Python  - Assignment 3 Problem 5
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

def maxheight(grid):
    nbr_rows = len(grid)   #number of rows
    nbr_columns = len(grid[0])  #number of columns
    sum = 0
    for i in range(nbr_rows):
        max = 0
        for j in range(nbr_columns):
            if grid[i][j] > max:
               max = grid[i][j]
 #       print('Max Number in Each Row: ', max)
        sum += grid[i][j]
        return sum

g = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
# print(grid[0])
answer  = maxheight(g)
print(answer)

"""
sum = 0
for row in grid:
    for element in row:
        print(element, end =' ')
        print()

for row in grid:
    print(' '.join([str(element) for element in row]))

# adds all elements
for row in grid:
    for element in row:
        sum += element
print(sum)

"""



