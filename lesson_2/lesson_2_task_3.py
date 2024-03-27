def square(side):
    area = round(side) * round(side)
    print(area)

    return area
side = float(input("Введите размер стороны: "))
print (square(side))