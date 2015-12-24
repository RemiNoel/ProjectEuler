# You are given the following information, but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

from math import floor

def day_of_the_week(day, month, year):
	# 	The formula to determine the day of the week is under Disparate variation 
	#	-> https://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week

	"""
	Y is the year minus 1 for January or February, and the year for any other month
	y is the last 2 digits of Y
	c is the first 2 digits of Y
	d is the day of the month (1 to 31)
	m is the shifted month (March=1,...,February=12)
	w is the day of week (0=Sunday,...,6=Saturday)
	"""
	d = day
	m = (month - 3) % 12 + 1
	
	# 	Based on the formula, January starts at 10
	if m > 10: Y = year - 1 
	else: Y = year

	y = Y % 100
	c = (Y - (Y % 100))/100

	w = (d + floor(2.6*m - 0.2) + y + floor(y/4) + floor(c/4) - 2*c) % 7

	return (w)


start_day = 0 
start_year = 1901

end_year = 2000


# Start the count
count = 0

# Compute the number of months starting on a given day of the week in a century
for year in range(start_year, end_year + 1):
	for month in range(1, 13):
		if day_of_the_week(1, month, year) == start_day : count += 1

print("The number of Sundays that fell on the first of the month during the twentieth century is :
      ", count)
