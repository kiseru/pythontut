import math


def circle_area(radius):
    return math.pi * radius * radius


print("Введите радиус круга:")
print(f"Площадь круга: {circle_area(float(input()))}")
print("Введите радиус второго круга:")
print(f"Площадь второго круга: {circle_area(float(input()))}")
