# Write the function matrixMultiply(m1, m2) that takes two 2d lists 
# (that we will consider to be matrices) and returns a new 2d list that 
# is the result of multiplying the two matrices. Return None if the 
# two matrices cannot be multiplied for any reason.


def fun_matrixmultiply(m1, m2):

    r1,r2,c1,c2=len(m1),len(m2),len(m1[0]),len(m2[0])

    if c1!=r2: return None

    result=[[0]*c2 for p in range(r1)]
    for i in range(r1):
        for j in range(c2):
            ans=0
            for k in range(c1):
                ans+=m1[i][k]*m2[k][j]
            result[i][j]=ans
    
    return result






