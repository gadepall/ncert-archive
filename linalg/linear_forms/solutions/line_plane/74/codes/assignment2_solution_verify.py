#We can verify the degree value by calculating the dot product using the cos value,
#and then comapring it with the dot product of the numpy function

def verifyDegree(x, y, deg_val):
    dot_prod = np.dot(x, y)
    calc_dot_prod_val = round(np.linalg.norm(x) * np.linalg.norm(y) * np.cos(np.deg2rad(deg_val)))
    if(dot_prod == calc_dot_prod_val):
        return True
    else:
        return False
        
        

a = np.array([2, 5, -3])
b = np.array([-1, 8, 4])
val = verifyDegree(a,b,62.05396983120793)
print(val)


c = np.array([2, 2, 1])
d = np.array([4, 1, 8])
val = verifyDegree(c,d,48.18968510422141)
print(val)
