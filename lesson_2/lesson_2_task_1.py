lst = [ '🍇', '🍑', '🍐', '🍊', '🍌', '🍎']
for index, element in enumerate(lst):
    if index == 0:
        print("Первый элемент:", element)
    if index == len(lst) - 1:
        print("Последний элемент:", element)

# print("Первый элемент", lst[0])
# print("Последний элемент", lst[-1])