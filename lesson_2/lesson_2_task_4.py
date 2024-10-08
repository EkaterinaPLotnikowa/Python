# 1. Напишите функцию fizz_buzz, которая принимает один аргумент — n (число).
# 2. Функция должна печатать числа от 1 до n. При этом:
#     1. если число делится на 3, печатать `Fizz`;
#     2. если число делится на 5, печатать `Buzz`;
#     3. если число делится на 3 и на 5, печатать `FizzBuzz`

def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 5 == 0 and n % 3 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


n = 10
fizz_buzz(n)