import numpy as np

a = np.array([
    [1, 2, 1],
    [2, -1, 1],
    [1, 1, -2]
])

b = np.array([3, 8, -5])

result = np.linalg.solve(a, b)

print("Розв'язок:", np.round(result, 2))
print("Перевірка:", np.allclose(a @ result, b))