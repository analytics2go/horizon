# CPSC-442-11/Python  - Assignment 1, Problem 4
# Author:  Wofford, Juana 1014901
#
# Problem:
# Calculate the speed for running a 10-kilometer race in 1 hours 5
# minutes 42 seconds.
# What is the average pace (time per mile in minutes and seconds)?
# What is the average speed in miles per hour?
# -----------------------------------------------------

# convert kilometers to miles 1.61 kilometers in a mile
distance_miles_ran = 10 / 1.61

# pace time; how fast need to run in seconds
# (hours * 60 * 60) + (minutes * 60) + seconds = time in seconds
pace_time_in_seconds = (1 * 60 * 60) + (5 * 60) + 42
# print('time in seconds' + str(pace_time_in_seconds))

# seconds per mile
seconds_per_mile = pace_time_in_seconds / distance_miles_ran

# convert seconds into minutes by dividing by 60
seconds_to_minutes = seconds_per_mile / 60

# pace per mile
print('\n Pace Per Mile in minutes: ' + str(seconds_to_minutes))
print('\n Pace per Mile in seconds: ' + str(pace_time_in_seconds))

# miles per hour
miles_per_hour = 60 / seconds_to_minutes
print('\n Miles Per Hour: ' + str(round(miles_per_hour, 2)))




