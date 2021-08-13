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
		return None
	if col==0:
		return 1
	if col-1 == row:
		return 1
	level = row
	triangle=[]
	for i in range(level):
		triangle.append([])
	for i in triangle:
		for j in range(row+1):
			i.append




			



	