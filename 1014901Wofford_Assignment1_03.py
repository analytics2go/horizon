# CPSC-442-11/Python  - Assignment 1, Problem 3
# Author:  Wofford, Juana 1014901
#
# Problem:
# I have started walking to home at 7:30 AM for the first mile at slow step
# (8 min:15 sec per mile), then 3 miles at speed (7 min:12 sec per mile),
#  what time do I get home for breakfast? (format output in hh: min)

# calculate walking
# divide the time to walk distance into 60, 60 minutes in an hour
# Then multiply the result by the number of
# miles walked, which gives the speed in MPH
start_walk = 7 + 30 / 60.0
slow_walk = (8 + 15 / 60.0) / 60.0
stride_walk = (7 + 12 / 60.00) / 60.0

# calculate time for breakfast
t = (start_walk + slow_walk +start_walk )* 60
print(t)