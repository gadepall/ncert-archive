import numpy as np

coefficient_matrix = np.array([
    [2, -1],
    [3, 1]
])
value_matrix = np.array([10, 5])

result = np.linalg.solve(coefficient_matrix, value_matrix)

print(result)

# output
# [ 3. -4.]