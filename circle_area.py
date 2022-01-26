import math


def circle_area(radius):
    return math.pi * radius * radius

print("Введите радиус круга:")
first_circle_radius = float(input())
first_circle_area = circle_area(first_circle_radius)
print(f"Площадь круга: {first_circle_area}")

print("Введите радиус второго круга:")
second_circle_radius = float(input())
second_circle_area = circle_area(second_circle_radius)
print(f"Площадь второго круга: {second_circle_area}")
