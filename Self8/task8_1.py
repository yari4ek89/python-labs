import numpy as np

grades = np.random.randint(0, 101, size=(2, 5, 7))

print("Усі оцінки:")
print(grades)

print("\n1 - Оцінки однієї групи")
print("2 - Оцінки за однією темою")
print("3 - Оцінки одного студента")
print("4 - Оцінки студента у групі")
print("5 - Оцінки групи за темою")
print("6 - Оцінки студента за темою")

choice = int(input("Оберіть варіант (1-6): "))

if choice == 1:
    group = int(input("Номер групи (0-1): "))
    print(grades[group])

elif choice == 2:
    topic = int(input("Номер теми (1-7): "))
    print(grades[:, :, topic - 1])

elif choice == 3:
    student = int(input("Номер студента (1-5): "))
    print(grades[:, student - 1, :])

elif choice == 4:
    group = int(input("Номер групи (0-1): "))
    student = int(input("Номер студента (1-5): "))
    print(grades[group, student - 1, :])

elif choice == 5:
    group = int(input("Номер групи (0-1): "))
    topic = int(input("Номер теми (1-7): "))
    print(grades[group, :, topic - 1])

elif choice == 6:
    student = int(input("Номер студента (1-5): "))
    topic = int(input("Номер теми (1-7): "))
    print(grades[:, student - 1, topic - 1])

else:
    print("Невірний варіант")