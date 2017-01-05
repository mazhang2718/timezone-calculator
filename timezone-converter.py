def fix_time(hour):
	if hour<0:
		hour = 24+hour
		post_time = 'PM'
		day = 'yesterday'
	elif hour<12:
		post_time = 'AM'
		day = 'today'
	elif hour<24:
		post_time = 'PM'
		day = 'today'
	elif (hour>=24):
		hour = hour-24
		post_time = 'AM'
		day = 'tomorrow'
	return hour, post_time, day

option = input("\n1: Convert from San Francisco to Chicago \n2: Convert from Chicago to San Francisco\n\nEnter an option: ")

date = input("\nEnter a time 'HH:MM'/'HH:MM PM' \n(eg: '13:30' or '1:30 PM'): ")
hour, minute = date.split(":")[0], date.split(":")[1]

if 'PM' or 'pm' in minute:
	PMConversion = True
else:
	PMConversion = False

hour = int(hour)
minute = int(minute[0:2])

if option==1:
	hour += 2 + PMConversion*12
	hour, post_time, day = fix_time(hour)
	print "\n%s in San Francisco is %i:%i (%i:%i %s) %s in Chicago" % (date, hour, minute, hour%12, minute, post_time, day)
elif option==2:
	hour += PMConversion*12 - 2
	hour, post_time, day = fix_time(hour)
	print "\n%s in Chicago is %i:%i (%i:%i %s) %s in San Francisco" % (date, hour, minute, hour%12, minute, post_time, day)


