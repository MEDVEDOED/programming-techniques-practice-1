# Практическая работа №1. Техники программирования.
# Суховеев Данила, группа 123_321.
# Вводи положительные размеры. Дробные числа записывай через точку.


def calculate():
    a = float(input("Введи первое основание трапеции a, см: "))
    b = float(input("Введи второе основание трапеции b, см: "))
    h = float(input("Введи высоту трапеции h, см: "))

    area = (a + b) * h / 2
    return area


def convert():
    centimeters = float(input("Введи длину в сантиметрах: "))

    inches = centimeters / 2.54
    return inches


print("Практическая работа №1")
print("Вводи положительные размеры, дробные числа — через точку.")
print("1. Считаем площадь трапеции")

area_result = calculate()
print(f"Площадь трапеции: {area_result:.2f} см²")

print()
print("2. Переводим сантиметры в дюймы")

inches_result = convert()
print(f"Длина в дюймах: {inches_result:.2f}")
