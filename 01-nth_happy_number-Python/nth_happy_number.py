# Write the function nth_happy_number(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:

# https://en.wikipedia.org/wiki/Happy_number#:~:text=In%20number%20theory%2C%20a%20happy,starting%20with%20and%20eventually%20reaches
# Read more about the happy number from the above link.

# assert(nth_happy_number(1) == 1)
# assert(nth_happy_number(2) == 7)
# assert(nth_happy_number(3) == 10)
# assert(nth_happy_number(4) == 13)
# assert(nth_happy_number(5) == 19)
# assert(nth_happy_number(6) == 23)
# assert(nth_happy_number(7) == 28)
# assert(nth_happy_number(8) == 31)



def ishappynumber(n):
	# your code goes here
	lst=[]
	while(True):
		sum=0
		while(n>0):
			sum+=(n%10)**2
			n=n//10
		# print(sum,"----------")
		if sum==1:
			return True
		else:
			if sum in lst:
				return False
			# print(sum)
			lst.append(sum)
			n=sum


def nth_happy_number(n):
	num=1
	cnt=0
	while(True):
		if ishappynumber(num) :
			cnt+=1
		if cnt==n:
			return num
		num+=1
