import sympy as sp
a,b,c = sp.symbols(['a','b','c'])
#Given matrices
A = sp.Matrix([[0,a,-b],[-a,0,-c],[b,c,0]])
print(A)
#Finding determinants
l = A.det()
if l==0:
  print(" the determinant is equal 0")
else:
  print(" the determinant is not to equal 0")
