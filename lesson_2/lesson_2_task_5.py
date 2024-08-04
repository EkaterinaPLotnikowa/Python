# Напишите функцию month_to_season(), которая принимает 1 аргумент — номер месяца — и возвращает название сезона, к которому относится этот месяц.
# Например, передаем 2, на выходе получаем «Зима».

def month_to_season(num_month):
    if num_month == 1 or num_month == 3 or num_month == 12:
        print("Зима")
    elif num_month == 3 or num_month == 4 or num_month == 5:
        print("Весна")
    elif num_month == 6 or num_month == 7 or num_month == 8:
        print("Лето")
    elif num_month == 9 or num_month == 10 or num_month == 11:
        print("Осень")
    else:
        print("Ошибка, такого месяца нет")
    
num_month = int(input("Введите номер месяца: "))
month_to_season(num_month)

# ВАРИАНТ 2
# def month_to_season(num_month):
#     if num_month in (12, 1, 2):
#         print("Зима")
#     elif num_month in (3, 4, 5):
#         print("Весна")
#     elif num_month in (6, 7, 8):
#         print("Лето")
#     elif num_month in (9, 10, 11):
#         print("Осень")
#     else:
#         print("Ошибка, такого месяца нет")

# num_month = int(input("Введите номер месяца: "))
# month_to_season(num_month)