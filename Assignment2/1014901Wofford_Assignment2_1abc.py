# CPSC-442-11/Python  - Assignment 2 Problem 1 a,b,c
# Author:  Wofford, Juana 1014901
#
# Program outputs structures using control statements
# -----------------------------------------
#  Problem a.
# following program prints out the following pattern using for loops:
# *
# **
# ***
# ****
# *****
x='*'
for i in range(1, 6):
    for j in range(i):
         print(x, end=' ')
    print()

# Problem b.
# following program prints out the following pattern using while :
"""
  *
 **
 ***
****
*****
"""
size = 5
i = 1
while size >= i:
    print(("*" * i).rjust(size))
    i += 1

# Problem c.
# following prints out the following pattern using for loop :
"""
 **
****
******
********
**********
"""
print('\n')
size=5
for i in range(size):
    print(" "*(size-1-i)+"**"*(i+1))