# Write the function pascalsTriangleValue(row, col) 
# that takes int values row and col, and returns the 
# value in the given row and column of Pascal's 
# Triangle where the triangle starts at row 0, and 
# each row starts at column 0. If either row or col 
# are not legal values, return None, instead of crashing. 

"""
1 1 N  N  N  N
1 2 1  N  N  N
1 3 3  1  N  N
1 4 6  4  1  N
1 5 10 10 5  1

"""

def fun_pascaltrianglevalue(row, col):
	if col-1>row:
		return 0
	if col==0:
		return 1
	triangle=[[0]*(row+2) for i in range(row+1)]
	for i in triangle:
		i[0]=1
	for i in range(1,row+1):
		for j in range(1, row+2):
			triangle[i][j]= triangle[i-1][j]+triangle[i-1][j-1]
	# print(triangle)
	return triangle[row][col]

print(fun_pascaltrianglevalue(1, 1))




			



	