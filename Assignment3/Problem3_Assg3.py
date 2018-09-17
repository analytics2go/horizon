# ----------------------------------------------
# CPSC-442-11/Python  - Assignment 3 Problem 1
# Author:  Wofford, Juana 1014901
#
# Program Problem 3
# Every website has subdomains associated with it. Count the number of hits
# to each of the sub-domains. The input would be like “100 www.facebook.com”,
#  integer and string pair. 100 is the number of
# hits to each of the subdomain. Write a function to accomplish this task
# -----------------------------------------------
"""
Example 1:
Input:
["100 www.facebook.com"]
Output:
["100 www.facebook.com", "100 facebook.com", "100 com"]
"""
#----------------------------------------------------------------

def domainhit(slist):
    slist = dict(slist)    # convert list to dictionary
    print(sitelist)

# get the visit number from the dictionary
    for x in slist:
        visit = slist[x]

    for visit, addr in slist.items():
         print("Site Address: " + visit + " " + addr)
         print(visit + " " + addr.split('.')[1] + '.' + addr.split('.')[-1])
         print(visit + " " + addr.split('.')[-1])

sitelist = [["100","www.facebook.com"],["900","google.mail.com"],
            ["50","yahoo.com"], ["1", "intel.mail.com"],
            ["5", "wiki.org"]]

# call the function to print strings
answer = domainhit(sitelist)