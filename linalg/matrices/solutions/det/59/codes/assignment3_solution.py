import numpy as np

coefficient_matrix = np.array([
    [2, -1],
    [3, 4]
])
value_matrix = np.array([-2, 3])

result = np.linalg.solve(coefficient_matrix, value_matrix)

print(result)

'''

Output: [-0.45454545  1.09090909]


'''