# CPSC-442-11/Python  - Assignment 1, Problem 3
# Author:  Wofford, Juana 1014901
#
# Problem:
# I have started walking to home at 7:30 AM for the first mile at slow step
# (8 min:15 sec per mile), then 3 miles at speed (7 min:12 sec per mile),
#  what time do I get home for breakfast? (format output in hh: min)
# --------------------------------------------------------------------------

# calculate walking
# divide the time to walk distance into 60, 60 minutes in an hour
# Then multiply the result by the number of
# miles walked, which gives the speed in MPH

start_walk = 7 + 30 / 60.0
slow_walk = (8 + 15 / 60.0) / 60.0
stride_walk = (7 + 12 / 60.00) / 60.0
speed_of_walk = (start_walk * 2 )+ ( stride_walk * 3)
# calculate time for breakfast
hour_breakfast = start_walk + speed_of_walk
minute_breakfast = (hour_breakfast-int(hour_breakfast))*60

# display breakfast time)
hour_breakfast = hour_breakfast - 12
breakfast_time = "%d:%02d" % (hour_breakfast, minute_breakfast)
print('\n Breakfast Time is: ' + breakfast_time)