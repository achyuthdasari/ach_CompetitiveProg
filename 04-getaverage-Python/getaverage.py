# Write the function getAverage(values) that takes a string of 
# comma-separated non-negative integer values, and returns their 
# average as a float (even though the values themselves are integers). 
# Note that some values may not be non-negative integers, and these 
# should be ignored. If there are no integer values, return 0 (do not crash here).
# For example, getAverage('13,excused,14,absent') ignores the two 
# strings and averages 13 and 14 to return 13.5. Also, getAverage('a,b,c') returns 0.


def fun_getaverage(s): 
	lst=s.split(",")
	print(lst)
	count=0
	sum=0
	for i in lst:
		try:
			sum+=int(i)
			count+=1
		except:
			continue
	if count==0:
		return 0.0
	return sum/count


fun_getaverage("1,2,3,4,5,6,7,8,9,10")
