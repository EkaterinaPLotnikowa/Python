# 1. Дано**:** пользователь делает вклад в размере Х рублей сроком на Y лет под 10% годовых 
# (каждый год размер его вклада увеличивается на 10%, эти деньги прибавляются к сумме вклада, 
# и на них в следующем году тоже будут проценты).
# 2. Задача: написать функцию bank, принимающую аргументы X и Y и 
# возвращающую сумму, которая будет на счету пользователя спустя Y лет.

def bank(x, y):
    for y in range(1, y + 1):
        x += x*0.1
        print(f"Year {y}: {x:.2f}", end="; ")

bank(1000, 2)