import numpy as np

numbers = input("Введіть числа: ")
numbers_array = np.fromstring(numbers, dtype=int, sep=" ")
values, counts = np.unique(numbers_array, return_counts=True)
index = np.argmax(counts)

print("Найчастіше число:", values[index])