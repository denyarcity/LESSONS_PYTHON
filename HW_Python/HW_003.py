# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

def sum_odd_index(lst):
    s = 0
    print('Позиция -> сумма позиций: ')
    for i in range(len(lst)):
        if i % 2 != 0:
            s += lst[i]
            print(i, end=' -> ')
            print(s, end='|')
    print(f"\nРезультат: = {s}")

lst = list(map(int, input("Введите числа через пробел:\n").split()))
sum_odd_index(lst)

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

def mult_lst(lst):
    l = len(lst)//2 + 1 if len(lst) % 2 != 0 else len(lst)//2
    new_lst = [lst[i]*lst[len(lst)-i-1] for i in range(l)]
    print(new_lst)

lst = list(map(int, input("Введите числа через пробел:\n").split()))
mult_lst(lst)

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

lst = list(map(float, input("Введите числа через пробел:\n").split()))
new_lst = [round(i%1,2) for i in lst if i%1 != 0]
print(max(new_lst) - min(new_lst))

#4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

s = ""
n = int(input("Введите число для преобразовывания десятичного числа в двоичное:\n"))
while n != 0:
    s = str(n%2) + s
    n //=2
print(s)

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def Fibonacci(n):
    if n in [1, 2]:                       
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

def NegaFibonacci(n):
    if n == 1:                       
        return 1
    elif n == 2:                       
        return -1
    else:
        num1, num2 = 1, -1
        for i in range(2, n):
            num1, num2 = num2, num1 - num2
        return num2

list = [0]
userNumber = int(input('Enter any number: '))
for e in range(1, userNumber + 1):
    list.append(Fibonacci(e))
    list.insert(0, NegaFibonacci(e))
print(list)