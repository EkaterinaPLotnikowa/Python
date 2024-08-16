# 1 Дан список lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20].
# 2. Выведите сумму всех элементов списка.

lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
total = 0

def sum_elements(lst):
    print(sum(lst))
sum_elements(lst)

# for num in lst:
#     total += num
# print("Сумма чисел в списке: ", total)