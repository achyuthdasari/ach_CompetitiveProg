# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).


def is_happy_num(n):
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
		# print(lst)

def is_prime(n):
	if n==2: return True
	elif n==1 or n==0: return False
	elif n%2==0: return False
	else:
		for i in range(3,int(n**0.5)+1,2):
			if n%i==0: return False
	return True

def fun_nth_happy_prime(n):
	num=1
	cnt=-1
	while(True):
		if is_prime(num) and is_happy_num(num) :
			cnt+=1
		if cnt==n:
			return num
		num+=1

	
