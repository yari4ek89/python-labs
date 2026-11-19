import numpy as np

grades = input("Введіть оцінки: ")
grades_array = np.fromstring(grades, dtype=int, sep=" ")
grades_array = np.where(grades_array < 60, 0, grades_array)
print(grades_array)
changed_sum = np.sum(grades_array == 0)
print("Замінено: ", changed_sum)