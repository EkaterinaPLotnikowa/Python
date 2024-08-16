import math


def square(side):
    area = side * side
    return area


side = float(input("Введите размер стороны: "))
area = square(side)
print("Округленная лощадь", math.ceil(area))
