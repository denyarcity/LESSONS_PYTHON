# print('hello world')

# # ---------- Типы данных и переменная
# # int, float, boolean, str, list, None

# a = 123
# b = 3.21
# print(a) # print выводит текст
# print(b)
# print(type(a)) # type определяет тип данных
# print(type(b))

# s = '"Французские булки очень вкусные \n---"'# \n перенос на новую строку
# print(s) # вывод строки

# print(a, '-', b, '-', s) # ковычки позволяют добавлять строки
# print('{2} - {1} - {0}'.format(a, b, s)) # аналогично предыдущему примеру, но через шаблон. Путем расстановки переменных мы можем менять порядок отображения.
# print(f'{a} - {b} - {s}') # еще один пример интерполяции

# f = True # присвоение логической переменной 
# print(f)



# list = [1,2,3] #создаем массив.
# col = ['hello', '1', '2','3'] # с помощью '' числа становятся строками
# print(list)
# print(col)


# ---------- Ввод и вывод данных
# input, print 

# print('Введие а');
# a = input()
# print('Введие b');
# b = input()
# print(a, b) # примеры вывода данных
# print('{1} {0}'.format(a,b))
# print(f'{a} {b}')

# print('Введие а');
# a = int(input()) # int - прием целочисленных значений
# print('Введие b');
# b = int(input())
# print(a, ' + ' ,b, ' = ', a+b) # примеры вывода данных

# print('Введие а');
# a = float(input()) # float - прием вещественных значений
# print('Введие b');
# b = float(input())
# print(a, ' + ' ,b, ' = ', a+b) # примеры вывода данных

# a = int(input('Введите число а: '))
# b = int(input('Введите число b: '))
# print(a, ' + ' ,b, ' = ', a+b)



# ---------- Арифметические операции
# +, -, *, /, %, //, **
# **, ⊕, ⊖, *, /, //, %, +, -
# ( ), сокращенные операции

# a = 10
# b = 3
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b) # деление дает вещественный результат по умолчанию
# print(a%b) # получить остаток от деления
# print(a//b) # целочисленный остаток от деления
# print(a**b) # a в степени b
# print(round(a/b,3)) # ограничиваем кол-во знаков посе запятой

#сокращенные операции
# a = 5
# a +=5 # вместо a=a+5. работает для всех типов арифметических операций
# print(a)

# ---------- Логические операции
# >, >=, <, <=, ==, !=
# not, and, or – не путать с &, |, ^
# Кое-что ещё: is, is not, in, not in

# a = (print('1 =', 1>4))
# a = (print('2 =', 1<4))
# a = (print('3 =',1>=4))
# a = (print('4 =',1<=4))
# a = (print('5 =',1==4))
# a = (print('6 =',1!=4))
# a = (print('7 =',1<4 and 5>2)) # и
# a = (print('8 =','текст'=='текст'))
# a = (print('9 =',[1,2]==[2,1])) # сравниваем массивы
# a = (print('10 =',1 < 3 < 5)) # тройное неравенство и более
# a = (print('11 =',1<4 or 5>2)) # или
# f = [1,2,3,4]
# print('Есть ли двойка в массиве: ',f, 'И это :',2 in f)
# print('Не хочу видеть двойку в массиве: ',f, 'И это :',not 2 in f)
# is_odd = f[0] == 1 # проверяем равенство числа по его индексу
# print(is_odd)



# ---------- Управляющие конструкции: if, if-else

# a = int(input('a = '))
# b = int(input('b = '))
# if a>b:
#     print(a)
# else:
#     print(b)

# username = input('Введите имя: ')
# if username == 'Денис':
#     print('Я так тебя ждал Денис!')
# elif username == 'Сергей':
#     print('Здарова Сергей!')
# elif username == 'Максим':
#     print('Как жизнь Максим?')
# else:
#     print('Привет, ', username)


# ---------- Управляющие конструкции:while
# Цикл позволяет выполнить блок операторов какое-то количество раз



# original = int(input('Введите целое число: '))
# inverted = 0
# while original !=0: # цикл выполняется до тех пор, пока original не станет = 0
#     inverted = inverted * 10 + (original % 10)
#     original //=10
# else:
#     num = int(input('Введите число, на которое хотите умножить инвертированный результат: '))
#     num2 = inverted * num
# print('Инвертированный результат = ', inverted)
# print('Резульат умножения = ', num2)


# ---------- Управляющие конструкции: for

# list = [1,2,3,4,9,5]
# for i in list:
#     print(i**2) # находим квадратный корень каждого числав массиве

# r = range(10)
# for i in r: # ранжируем числа от 0 до 10 и выводим их по порядку
#     print(i)

# for i in range(2, 11, 2): # ранжируем по порядку четные числа от 2 до 11
#     print(i)

# for i in 'qwerty': # разбивка текста по символам
#     print(i)


# ---------- Немного о строках

# text = 'съешь ещё этих мягких французских булок'
# print(len(text)) # 39
# print('ещё' in text) # True
# print(text.isdigit()) # False
# print(text.islower()) # True
# print(text.replace('ещё','ЕЩЁ')) #
# for c in text:
#     print(c)
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # print(text)
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...


# ---------- Списки: введение

# numbers = [1, 2, 3, 4, 5]
# print(numbers) # [1, 2, 3, 4, 5]
# numbers = list(range(1, 6))
# print(numbers) # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(numbers) # [10, 2, 3, 4, 5]
# for i in numbers:
#  i *= 2
#  print(i) # [20, 4, 6, 8, 10]
# print(numbers) # [10, 2, 3, 4, 5]


# colors = ['red', 'green', 'blue']
# for e in colors:
#  print(e) # red green blue
# for e in colors:
#  print(e*2) # redred greengreen blueblue
# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # удалить элемент


# ---------- Функции

def f(x):
    return x**2
def f(x):
 if x == 1:
    return 'Целое'
 elif x == 2.3:
    return 23
 else:
    return
print(f(1)) # Целое
print(f(2.3)) # 23
print(f(28)) # None
print(type(f(1))) # str
print(type(f(2.3))) # int
print(type(f(28))) # NoneTyp



