import numpy as np
import time

grades = np.random.randint(0, 101, size=(30, 200, 20))

topic = int(input("Введіть номер теми (1-20): "))

if 1 <= topic <= 20:
    topic -= 1
    repeats = 100

    start = time.perf_counter()

    for _ in range(repeats):
        result_for = []
        for group in range(30):
            students = []
            for student in range(200):
                students.append(grades[group, student, topic])
            result_for.append(students)
        result_for = np.array(result_for)

    time_for = (time.perf_counter() - start) / repeats

    start = time.perf_counter()

    for _ in range(repeats):
        result_slice = grades[:, :, topic].copy()

    time_slice = (time.perf_counter() - start) / repeats

    print("Час через for:", time_for)
    print("Час через зріз:", time_slice)
    print("Результати однакові:", np.array_equal(result_for, result_slice))
else:
    print("Невірний номер теми")