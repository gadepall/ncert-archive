# To check the particular solution being right, we can cross verify the result as follows:

# Given set of vectors
a = [1, 4, 2]
b = [3, -2, 7]
c = [2, -1, 4]

# Resultant vector we computed
d = [ 53.33333333,  -1.66666667, -23.33333333]

# Checking the corresponding dot product 
print(np.dot(a,d))
print(np.dot(b,d))
print(np.dot(c,d))
