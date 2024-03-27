lst = [ '🍇', '🍑', '🍐', '🍊', '🍌', '🍎']
for index, element in enumerate(lst):
    if index == 0:
        print("Первый элемент:", element)
    if index == len(lst) - 1:
        print("Последний элемент:", element)