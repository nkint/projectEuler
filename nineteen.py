# year month day

from datetime import date, timedelta

#start = date(1901, 1, 1)
#arrival = date(2000, 12, 31)
#oneday = date(1,1,2)-date(1,1,1)

#sundays = 0
#while start<arrival:
#	start += oneday
#	if start.weekday()==6 and start.day==1: 
#		sundays+=1
#		print(start)

import itertools as it
ym = it.chain(*[[(y,m) for m in range(1,13)] for y in range(1901, 2001)])
days = [date(y,m,1) for y,m in ym]
sundays = len(list(filter(lambda d: d.weekday()==6, days)))

print(sundays)
