# CPSC-442-11/Python  - Assignment 2 Problem 4
# Author:  Wofford, Juana 1014901
#
# Given a positive integer, output its 2’s complement number. The 2’s
# complement strategy is to flip the bits of its binary representation
# and then add 1 to the binary representation.
# You need to write the definition for the method find2sComplement().
#
# -----------------------------------------


# find ones compliment

def find2sComplement(num):
    #Folloing method would return the 2's complement of the decimal number
    numWord = bin (num)  # changing to binanry
    length = len(numWord) # get the length
    i = 0
    result = ''

    length = length -1
    while i < length:
            if numWord[i]=='1':
                result = '1'
                return result
            else:
                if






def findComplement(num):
    # Following method would return the 1's complement of the decimal number
    numWord = bin(num)   # converts decimal number to binary representation
    numWord = numWord[2:]  # trims initial 2 chars from string
    length = len(numWord)  # calculates the length of the string
    i = 0
    res = ''
    # Following loop would iterate for every char to convert it
    while i < length:
            if numWord[i]=='1':
                    res+='0'
            else:
                    res+='1'
            i+=1
    return res



# complement =  findComplement(num)
result = findComplement(10)
print('answer is: ' + str(result))

x = to_int(result)
print('\n next answer is: '+ str(x))

