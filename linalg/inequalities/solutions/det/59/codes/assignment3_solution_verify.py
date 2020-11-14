def eqnValChecker(x_val, y_val):
    eqn1 = round(2*(x_val) - y_val)
    eqn2 = round(3*(x_val) + 4*(y_val))

    if (eqn1 == -2) and (eqn2 == 3):
        return True
    else:
        return False
		
print(eqnValChecker(-0.45454545, 1.09090909))

'''
Output: True
'''