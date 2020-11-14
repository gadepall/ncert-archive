from sympy import Matrix, Rational

V = Matrix([[6, Rational(17,2)],[Rational(17,2), 12]])

Q, R = V.QRdecomposition()

print(Q)
print(R)