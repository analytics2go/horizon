# ----------------------------------------------
# CPSC-442-11/Python  - Assignment 3 Problem 6
# Author:  Wofford, Juana 1014901
# Problem 6
# Given an array of strings, group anagrams together.
# Your task is to write a function to accomplish this task.
#
"""
Example: Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output: [   ["ate","eat","tea"],   ["nat","tan"],   ["bat"] ]
"""
# ------------------------------

# iterator that returns consecutive keys and groups
# from the iterable
from itertools import groupby

def groupAnagramWords(inlist):
    # inlist is the iterable data set
    # looping through the keys and the groups of data (inlist)
    # then using groupby to loop through the sorted data
    x = [list(group) for key, group in
                groupby(sorted(inlist, key = sorted), sorted)]
    return x

inlist = ["eat", "tea", "tan", "ate", "nat", "bat"]
print('\n List of Words: ',inlist)
answer = groupAnagramWords(inlist)
print('\nHere are the Anagrams from the List of Words:')
print(answer)
print()


