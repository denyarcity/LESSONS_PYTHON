# ---------- 1. Файлы
# a – открытие для добавления данных
# r – открытие для чтения данных
# w – открытие для записи данных
# w+, r+

# colors = ['red','green','blue']
# data = open('color.txt', 'w') # создаем файл
# data.writelines(colors)  # записываем данные в одну строку. разделители не будут записаны
# data.write('\nLine1\n') # переносим и записываем на новые строки
# data.write('Line2\n')
# data.close()  # разрываем соединение файловой переменной с файлом на диске, во избежание утечек памяти


# воспринимаем как переменную data. В таком случае не нужно в конце указывать data.close(), программа завершится сама.
# with open('color.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')

# colors = ['red', 'green', 'blue\n']
# data = open('color.txt', 'a')
# data.writelines(colors)  # разделителей не будет
# data.close()

# path = 'color.txt' # путь к файлу
# data = open(path, 'r') # отрываем в режиме чтения
# for line in data: # с помощью цикла бежим по файлу
#  print(line) # и считываем строки
# data.close() # разрываем связь


# ---------- 2. Функции и модули


# # с помощью import, можно пользоваться функциями находящимися в других файлах
# import Example_001_Hello
# print(Example_001_Hello.f(1))

# # в данном случае мы сокращаем наименование файла для простоты вызова
# import Example_001_Hello as Ex1
# print(Ex1.f(1))


# def new_string(symbol, count):
#     return symbol * count
# print(new_string('!',5)) # выводим пять символов

# def new_string(symbol, count = 3):
#     return symbol * count
# print(new_string('!')) # выводим три символа
# print(new_string(4)) # умножаем на число в скобках т.к. числовой формат.

# def concatenatio(*params):  # возможность передачи неограниченного кол-ва аргументов *params
#     res: str = ""
#     for item in params:
#         res += item
#     return res

# print(concatenatio('a', 's', 'd', 'w'))  # asdw
# print(concatenatio('a', '1', 'd', '2'))  # a1d2
# # print(conatenatio(1, 2, 3, 4)) # TypeError: ...

# def concatenatio(*params): # вариация для чисел
#     res: int = 0
#     for item in params:
#         res += item
#     return res

# print(concatenatio(1, 2, 3, 4)) #= 10


# ---------- 3. Рекурсия


# Вычисление чисел Фибаначи
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)


# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list)  # 1 1 2 3 5 8 13 21 34


# ---------- 4. Кортеж – это неизменяемый “список”


# t = ()
# print(type(t))  # tuple
# t = (1,)
# print(type(t))  # tuple
# t = (1)
# print(type(t))  # int
# t = (28, 9, 1990)
# print(type(t))  # tuple
# colors = ['red', 'green', 'blue']
# print(colors)  # ['red', 'green', 'blue']
# t = tuple(colors)
# print(t)  # ('red', 'green', 'blue')
# t = tuple(['red', 'green', 'blue'])
# print(t[0])  # red
# print(t[2])  # blue
# # print(t[10]) # IndexError: tuple index out of range
# print(t[-2])  # green
# # print(t[-200]) # IndexError: tuple index out of range
# for e in t:
#     print(e)  # red green blue
# t[0] = 'black'  # TypeError: 'tuple' object does not support item assignment


# --------- 5. Cловари


# Неупорядоченные коллекции произвольных объектов с доступом по ключу


# dictionary = {}
# dictionary = \
#     {
#         'up': '↑', # up это ключ, а символ справа это элемент доступный по ключу
#         'left': '←',
#         'down': '↓',
#         'right': '→'
#     }
# print(dictionary)  # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left'])  # ←
# # типы ключей могут отличаться

# for k in dictionary.keys(): # перечисляем ключи
#     print(k,end=' ')
# for k in dictionary.values(): # перечисляем значения
#     print(k,end=' ')

# print(dictionary['up'],) # ↑
# # типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# #print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента
# for item in dictionary: # for (k,v) in dictionary.items():
#  print('{}: {}'.format(item, dictionary[item]))
# # up: ↑
# # down: ↓
# # right: →


# ---------- 6. Множества


# colors = {'red', 'green', 'blue'}
# print(colors)  # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors)  # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors)  # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors)  # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red'
# colors.discard('red')  # ok
# print(colors)  # {'green', 'blue','gray'}
# colors.clear()  # { }
# print(colors)  # set()


# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q = a \
#  .union(b) \
#  .difference(a.intersection(b))
# # {1, 21, 3, 13}

# a = {1, 2, 3, 5, 8} # Замороженное множество не подвержено изменениям
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3, 5, 8})

# ---------- 7. Списки

# list1 = [1, 2, 3, 4, 5]
# list2 = list1 # копируем массив
# print(list1) # выводится массив
# print(list2)

# list2[1] = 123 # меняем число под индексом [0], число меняется в обоих массивах
# list1[0] = 321

# for e in list1:
#     print(e, end=' ') # выводятся числа

# print()

# for e in list2:
#     print(e, end=' ')


list1 = [1, 2, 3, 4, 5, 6]

print(list1)
print('Последнее число в массиве: ',list1.pop()) # pop извлекает последний элемент и удаляет его
print('осталось символов в массиве: ',len(list1))
print('внеплановое удаление символа под индексом 2: ',list1.pop(2))
print(list1)
print('Последнее число в массиве: ',list1.pop())
print('осталось символов в массиве: ',len(list1))
print('внеплановое возвращение символа под индексом 2: ',list1.insert(2, 3))
print(list1)
print('Последнее число в массиве: ',list1.pop())
print('осталось символов в массиве: ',len(list1))
print(list1)
print('Последнее число в массиве: ',list1.pop())
print('осталось символов в массиве: ',len(list1))
print(list1)
print('Последнее число в массиве: ',list1.pop())
print('осталось символов в массиве: ',len(list1))