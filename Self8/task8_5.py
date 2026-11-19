import numpy as np

grades = np.array([
    [80, 70, 90],
    [95, 100, 65],
    [60, 85, 70]
])

average_student = np.round(np.mean(grades, axis=1), 2)
print("Середні бали: ", average_student)
best_student = np.argmax(average_student) + 1
print("Найкращий студент: ", best_student)
average_subject = np.round(np.mean(grades, axis=0), 2)
lower_average = np.where(average_subject < np.mean(grades))[0] + 1
print("Предмети нижче середнього: ", lower_average)