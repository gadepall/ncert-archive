def findDegree(a, b):
    dot_prod = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    inv_val = dot_prod / (norm_a * norm_b)
    radian_val = np.arccos(inv_val)
    deg_val = np.degrees(radian_val)
    return deg_val
	
	
a = np.array([2, 5, -3])
b = np.array([-1, 8, 4])
deg_val_ab = findDegree(a, b)
print(deg_val_ab)

'''

Ouptut:- 62.05396983120793

'''

c = np.array([2, 2, 1])
d = np.array([4, 1, 8])
deg_val_cd = findDegree(c, d)
print(deg_val_cd)

'''

Output: 48.18968510422141

'''
