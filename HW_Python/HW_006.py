# Задача: предложить улучшения кода для уже решённых задач: С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

import random

lst = [random.randrange(1, 10, 1) for i in range(8)]
print(lst)
res = [x for x in lst if lst.count(x) == 1]
print(res)

# Найти сумму чисел списка стоящих на нечетной позиции

lst = list(map(int, input('Введите числа через пробел: ').split()))
print(f'Сумма элементов списка, стоящих на нечётной позиции: {sum(lst[1::2])}')

# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = list(input('Введите текст содержащий последовательность "абв": ').split())
result = ' '.join(filter(lambda x: 'абв' not in x, text))
print(result)