# makeMagicSquare(n)
# Write the function makeMagicSquare(n) that takes a positive 
# odd integer n and returns an nxn magic square by following 
# the resource here. If n is not a positive odd integer, 
# return None.

# URL: https://en.wikipedia.org/wiki/Magic_square

# Hints: From Geeks for Geeks.
# Did you find any pattern in which the numbers are stored? 

# In any magic square, the first number i.e. 1 is 
# stored at position (n/2, n-1). Let this position 
# be (i,j). The next number is stored at position (i-1, j+1) 
# where we can consider each row & column as circular array 
# i.e. they wrap around.

# Three conditions hold:

# 1. The position of next number is calculated by 
# decrementing row number of the previous number by 1,
#  and incrementing the column number of the previous 
# number by 1. At any time, if the calculated row position 
# becomes -1, it will wrap around to n-1. Similarly, if 
# the calculated column position becomes n, it will wrap 
# around to 0.

# 2. If the magic square already contains a number at the 
# calculated position, calculated column position will be 
# decremented by 2, and calculated row position will be 
# incremented by 1.

# 3. If the calculated row position is -1 & calculated 
# column position is n, the new position would be: (0, n-2). 

def makeMagicSquare(n):
    # Your code goes here...
    if n<0 or n%2==0:
        return None
    square=[[0]*n for i in range(n)]
    
    square[n//2][n-1]=1
    a=n//2
    b=n-1

    for i in range(2, n*n+1):
        a=a-1
        b=b+1
        # print(a,b)
        if a==-1 and b==n:
            a=0
            b=n-2
        elif a<0:
            a=n+a
        elif b>n-1:
            b=b-n
        if square[a][b]==0:
            square[a][b]=i
        else:
            b=b-2
            if b<0:
                b=n+b
            a=a+1
            if a>n-1:
                a=a-n+1
            square[a][b]=i
        # print(square)
    return square


def ismostlymagicsquare(a):
	# Your code goes here
	sum=0
	for i in a[0]:
		sum+=i
	for i in a:
		curr=0
		for j in i:
			curr+=j
		if curr!=sum:
			return False
	
	for i in range(len(a)):
		curr=0
		for j in range(len(a)):
			curr+=a[j][i]
		if curr!=sum:
			return False

	curr=0
	for i in range(len(a)):
		curr+=a[i][i]
	if curr!=sum:
		return False
	
	curr=0
	for i in range(len(a)):
		curr+=a[i][len(a)-1-i]
	if curr!=sum:
		return False
	return True
            

print(ismostlymagicsquare(makeMagicSquare(3)))
print(ismostlymagicsquare(makeMagicSquare(5)))
print(ismostlymagicsquare(makeMagicSquare(15)))


        


