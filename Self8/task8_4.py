import numpy as np

numbers = input("Введіть числа: ")
numbers_array = np.fromstring(numbers, dtype=int, sep=" ")
minimal_number = np.min(numbers_array)
maximum_number = np.max(numbers_array)
if maximum_number == minimal_number:
    print("Усі значення однакові.")
else:
    normalized = np.round((numbers_array - minimal_number) / (maximum_number - minimal_number), 2)
    print(normalized)