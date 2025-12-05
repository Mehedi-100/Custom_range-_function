def my_range(start, end = None, step = 1):
	if end is None:	#check for single value 
		end = start
		start = 0
	current = start
	if step > 0:	#in case positive step
		while current < end:
			yield current
			current+=step
	else:	#in case negative step
		while current > end:
			yield current 
			current+=step

for i in my_range(7):
	print(i,end = ' ')
	
print()

for i in my_range(5,20,3):
	print(i, end = ' ')

print()

for i in my_range(40,5,-5):
	print(i, end = ' ')
