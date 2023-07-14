from linear_algebra import *
from mod import *

"""
mod = 2
Modint(m=mod)
N = 4
A = [[Modint(0) for i in range(N*N)] for j in range(N*N)]
for i in range(N*N):
    A[i][i] = Modint(1)
    if(i%N != 0):     A[i][i-1] = Modint(1) 
    if((i+1)%N != 0): A[i][i+1] = Modint(1) 
    if(i+N <  N*N):     A[i][i+N] = Modint(1)
    if(i-N >= 0):     A[i][i-N] = Modint(1)
print("A")
for i in A: print(i)



b = [[Modint(0)] for i in range(16)]        
b[0][0] = Modint(1)
b[1][0] = Modint(1)
b[4][0] = Modint(1)

x =  SimultaneousEquationsSolver(A,b)
print(x)
"""
x = 1
if x: print("YES")
x = True
if x: print("Yes")

print(1^1)


