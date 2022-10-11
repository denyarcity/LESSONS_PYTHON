# 1. Анонимные, lambda функции

# ----------- пример 1

# def f(x):
#     return x**2 # возводим х в квадрат

# g = f # присваиваем функцию f в переменную g

# print(type(f)) # выводим тип функции
# print(type(g))

# print(f(4)) # присваиваем х = 4 и видим что обе f и g работают одинаково.
# print(g(4))

# ----------- пример 2

# def calc1(x): # переменная calc, которая принимает в качестве аргумента число x
#     return x+10 # в качестве результата возвращает x+10
# print (calc1(10))

# def calc2(x): # переменная calc, которая принимает в качестве аргумента число x
#     return x*10 # в качестве результата возвращает x+10
# print (calc2(10))

# def math(op,x): # функция def math, где в качестве аргумента приходит операция и число x
#     print(op(x)) # вызываем функцию op и передаем в неё аргумент x

# math (calc2, 10)
# math (calc1, 10)

# ----------- пример 3

# def sum(x,y):
#     return x+y

# sum = lambda x, y: x+y # то же самое что написано на 34 - 35 строке

# def mylt(x,y):
#     return x*y

# def calc(op, a, b):
#     print(op (a,b))
#     #return op(a,b)

# calc(mylt, 4, 5)
# # calc(sum, 4, 5)

# calc(lambda x, y: x+y, 4, 5) # альтернатива 37 и 47 строке

# 2. Функция map

# Функция map() применяет указанную функцию к
# каждому элементу итерируемого объекта и
# возвращает итератор с новыми объектами.

# li = [x for x in range(1,21)]
# li = list(map(lambda x:x+10, li))
# print (li)

# 3. Функция filter

# Функция filter() применяет указанную функцию к
# каждому элементу итерируемого объекта и
# возвращает итератор с теми объектами, для
# которых функция вернула True.

# data = [x for x in range(1, 11)]

# res = list(filter(lambda x: not x%2, data))
# print (res)

# 4. Функция zip

# Функция zip() применяется к набору итерируемых
# объектов и возвращает итератор с кортежами из
# элементов входных данных.

# from collections import UserString

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]

# data = list(zip(users, ids, salary))
# print(data)

# 5. Функция enumerate

# Функция enumerate() применяется к итерируемому
# объекту и возвращает новый итератор с кортежами
# из индекса и элементов входных данных.

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]

data = list(enumerate(users))
print(data)

# 6. List Comprehension

# list = []
# for i in range(1, 21):
#     if(i%2 == 0):
#         list.append(i)

# print(list)

# list = [i for i in range(1, 21) if i %2 == 0] # аналогично коду 69 - 74 строке
# print(list)

# ----------- пример 2

# import re


# def f(x):
#     return x**3

# list = [(i, f(i)) for i in range(1, 21) if i %2 == 0] # в итоге число, которое делится на два без остатка и рядом куб этого числа
# print(list)

# ----------- пример 3

# list = [1, 2, 3, 5, 8, 15, 23, 38]
# f = lambda x: x**2
# numbrs = [(list[i], f(list[i])) for i in range (len(list)) if not (list[i] % 2)]
# print(numbrs)
