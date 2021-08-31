# Write the function hasnoprimes(L) that takes a 2d list L of integers, 
# and returns True if L does not contain any primes, and False otherwise.



def is_prime(n):
	if n==2: return True
	elif n==1 or n==0: return False
	elif n%2==0: return False
	else:
		for i in range(3,int(n**0.5)+1,2):
			if n%i==0: return False
	return True

def fun_hasnoprimes(l):
	for i in l:
		for j in i:
			if is_prime(j):
				return False
	return True

