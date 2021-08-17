# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	# your code goes here
	dictin={}
	high=0
	for i in str(n):
		if i not in dictin:
			dictin[i]=1
		else:
			dictin[i]+=1
		if dictin[i]>=high:
			high=dictin[i]
	lst=[]
	for i in dictin:
		if dictin[i]==high:
			lst.append(i)
	
	lst=sorted(lst)
	return int(lst[0])


	



