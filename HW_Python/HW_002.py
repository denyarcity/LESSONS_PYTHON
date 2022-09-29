# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

float_num = input('Введите число: ')
sum = 0
for i in float_num:
    if i != '.':
        sum += int(i)
print('Сумма цифр в числе = ', sum)


# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

n = int(input('Введите число N: '))
factorial = 1
for i in range(1, n+1):
    factorial *= i
    print(factorial, end=' | ')


# 3. Задайте список из n чисел последовательности 〖(1+1/n)〗^n и выведите на экран их сумму.

n = int(input("Введите число n: "))
s = 0
for i in range(1, n+1):
    s += (1+1/i)**i
    print(s, end=' | ')
print(f"\nПолученная сумма последовательности (1+1/n)^n равнна {round(s,2)}")

# 4. Задайте число N, создайте список: [-N, N]. Найдите произведение элементов на указанных позициях. Позиции (случайные) хранятся в файле file.txt (создаётся во время выполнения кода и зависит от количества элементов в списке) в одной строке одно число.

# Значения создаются рандомно и записываются в автоматический созданный txt файл
import random
def write_file(number):
    with open('file.txt', 'w') as data:
        for i in range(number):
            data.write(f"{random.randrange(0, 2*number)}\n")


def read_file():
    with open('file.txt', 'r') as data:
        indexs = list(map(int,data.readlines()))
    return indexs

n = int(input("Введите число N: "))
lst_number = [i for i in range(-n, n+1)]
write_file(n)
lst_index = read_file()
prod = 1
for i in range(len(lst_index)):
    prod *= lst_number[lst_index[i]]
print(f"Результат равен = {prod}")

# 5. Реализуйте алгоритм перемешивания списка.

import random
list = [1, 2, 3, 'Hello', 4, 5, 100]
print(list, end='')
random.shuffle(list)
print(' -> ', list)
