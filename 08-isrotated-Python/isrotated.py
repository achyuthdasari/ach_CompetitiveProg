# isRotated(str1, str2) [10 pts]
# Write an efficient program to test if two given String is a rotation of each other or not, e.g. 
# if given String is "XYZ" and "ZXY" then your function should return true, but if the input is 
# "XYZ" and "YXZ" then return false.


def isrotated(str1, str2):
	#Your code goes here
	if len(str1)!=len(str2):
		return False
	for i in range(len(str1)):
		if str1[i]==str2[0]:
			cnt=1
			for j in range(1,len(str1)):
				p=i+j
				if p>len(str1)-1:
					p=i+j-len(str1)
				if str1[p]==str2[j]:
					cnt+=1
				else: break
			if cnt==len(str1): return True
	return False

