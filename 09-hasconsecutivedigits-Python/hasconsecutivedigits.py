# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	# your code goes here
	strin=str(abs(n))
	lst=[]
	for i in strin:
		if i in lst:
			return True
		lst.append(i)
	return False
