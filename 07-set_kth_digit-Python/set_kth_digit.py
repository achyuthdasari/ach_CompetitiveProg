# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 



def fun_set_kth_digit(n, k, d):
	flag=0
	if n<0:
		flag=1
	n=str(abs(n))
	if k<len(n):
		ans=n[:len(n)-k-1]+str(d)+n[len(n)-k:]
	else:
		ans=str(d)+'0'*(k-len(n))+n
	if flag==0:
		return int(ans)
	else:
		return int(ans)*-1

print(fun_set_kth_digit(586, 4, 9))
	


