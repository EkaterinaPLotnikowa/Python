##students = ["Алексей", "Наталья", "Олег", "Екатерина", "Филипп", "Виктор"]

##for i in range(0,len(students)):
   ##print(students [i])

my_list = [1, 2, 3, 4, 5]
 
for i in my_list:
    if i == 6:
        print("Item found!")
        break
    print(i)
else:
    print("Item not found!")