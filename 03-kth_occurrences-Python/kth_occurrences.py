# Given a string str and an integer K, the task is to find the K-th most 
# frequent character in the string. If there are multiple characters that 
# can account as K-th the most frequent character then, print any one of them.



def fun_kth_occurrences(s, n):
	dictin={}
	for i in s:
		if i in dictin:
			dictin[i]+=1
		else:
			dictin[i]=1
	print(dictin)
	
	num=1
	def funct(i):
		return dictin[i]
	for j in sorted(dictin, key=funct,reverse=True):
		if num==n:
			return j
		num+=1
print(fun_kth_occurrences("helllo woorld", 2))


