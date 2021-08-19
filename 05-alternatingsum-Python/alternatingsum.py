# Write the function alternatingSum(a) that takes a list of numbers and returns the 
# alternating sum (where the sign alternates from positive to negative or vice versa). 
# For example, alternatingSum([5,3,8,4]) returns 6 (that is, 5-3+8-4). If the list is empty, return 0.




def fun_alternatingsum(a): 
	sum=0
	if len(a)%2==0:
		for i in range(0,len(a),2):
			sum+=(a[i]-a[i+1])
		return sum
	else:
		for i in range(0,len(a)-1,2):
			sum+=(a[i]-a[i+1])
		return sum+a[-1]

print(fun_alternatingsum([5,3,8,4,3]))




