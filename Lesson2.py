# list_1 = [] создание пустого списка
# list_1 = list()
# list_1 = [1 , 2 , 3 ,8]
# print(list_1)
# print(*list_1) #без Скобок будет выводиться

# for i in list_1:
#     print(i)
# print(len(list_1))
# print(list_1[0]) #обращение к элементу
# print(list_1[-1]) # индексация с конца

# list_1 = [1, 5]
# print(list_1)
# list_1.append(8)#append добавляет
# print(list_1)


# list_1 = []
# print(list_1)
# for i in range(5):
#     list_1.append(i)
#     print(list_1)

# Удаление последнего элемента списка. 
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop()) #0
# print(list_1) # [12, 7, -1, 21]
# print(list_1.pop()) # 21
# print(list_1) # [12, 7, -1]
# print(list_1.pop()) # -1
# print(list_1) # [12, 7]

# list_1 = [12, 7, -1, 21, 0]#pop удаляет последний элемент и возвращает
# a = list_1.pop() 
# print(a)

# Добавление элемента на нужную позицию
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.insert(2, 11))#2- позиция 11- значение
# print(list_1) # [12, 7, -1, |1, 21, 0]
# Срезы в списках
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[0]) # 1
# print(list_1[1]) # 2
# print(list_1[len(list_1)-1]) # 10
# print(list_1[-5]) # 6
# print(list_1[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[:2]) # [1, 2]
# print(list_1[len(list_1)-2:]) #[9, 10]
# print(list_1[2:9]) # [3, 4, 5, 6, 7, 8, 9]
# print(list_1[6:-18]) # []
# print(list_1[0:len(list_1):6]) # [1, 7]
# print(list_1[::6]) # [1, 7]

# t =()#создание пустого кортежа

# print(type(t))# выводить тип переменной t
# t = (1,)
# print(type(t))

# v = [1, 8, 9]
# print(v)
# print(type(v))

# v = tuple(v)#преобразование списка в кортеж
# print(v)
# print(type(v))

# a,b,c = v
# print(a,b,c)

# t = (1,2,3,5,)

# for i in t:#выводить кортеж
#     print(i)

# for i in range(len(t)):# выводить список
#     print(t[i])

# t = [1,2,3,5,]
# t[0] = 2
# print(t)

# d ={}#создание пустого словаря
# d =dict()# тоже словарь
# d['q'] = 'qwerty'#добавлять значения по ключу
# print(d)

# d['w'] = 'werty'#добавлять значения по ключу, выводяться ключ 
# #двоеточие значение
# print(d)


# dictionary = {}
# dictionary ={'up': 't', 'left': '+', 'down': '', 'right': '+'}
# print(dictionary) # {'up':'\', 'left':'+', 'down':''', 'right':'~'}
# print(dictionary['Left']) #
# # типы ключей могут отличаться
# print(dictionary['up']) #
# # типы ключей могут отличаться
# dictionary['left'] = '='
# print(dictionary['left']) # <
# print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента
# for item in dictionary:
# # for (k,v) in dictionary.items():
# print('{}: {}'.format(item, dictionary[item]))
# # up: 1
# # down: 
# # right: -


# colors = {'red', 'green', 'blue'} #создание множества
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')#add добавляет
# print(colors) # {'red', 'green', "blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red') # remove удаляет значение
# print(colors) # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok discard проверяет есть ли значение 
# # в множестве и удаляет
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { }clear чтобы удалить все элементы множества
# print(colors) # set()

# Операции со множествами в Python
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = а.сору() # c = {1, 2, 3, 5, 8}копировать
# u = a.union(b)  # u = {1, 2, 3, 5, 8, 13, 21} обьединение
# i = a.intersection(b) # i = {8, 2, 5}пересечение
# dl = a.difference(b) # dl = {1, 3}разность a-b
# dr = b.difference(a) # dr = {13, 21}разность b-a
# q=a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13}


# a = {1, 8, 6}

# b = frozenset(a) # замороженное множество не можем изменять
# print(b)

#  Создать список чисел от 1 до 100
# list_1 = []
# for i in range(1, 101):
# list_1.append(i)
# print(list_1) # [1, 2, 3,..., 100]
# Эту же функцию можно записать так:
# list_1 = [i for i in range(1, 101)] # [1, 2, 3,..., 100]

# Добавить условие (только чётные числа)
# list_1 = [i for i in range(1, 101) if i % 2 == 0] # [2, 4, 6,..., 100]
# Допустим, вы решили создать пары каждому из чисел (кортежи)
# list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0] # [(2, 2), (4, 4),...,
# (100, 100)]
# Также можно умножать, делить, прибавлять, вычитать. Например, умножить
# значение на 2.
# list_1 = [i * 2 for i in range(10) if i % 2 == 0]
# print(list_1) # [0, 4, 8, 12, 16]


# # Syntax Error(Синтаксическая ошибка)
#number_first = 5
#number_second = 7
# if number_first > number_second # !!!!!
#print(number_first)
# Отсутствие :

# # IndentationError(Ошибка отступов)
# number_first = 5
#number_second = 7
# if number_first > number_second:
#print(number_first) # !!!!!
# # Отсутствие отступов


# # # # Typeerror(Типовая ошибка)
# text = 'Python'
# number = 5
# print(text + number)
# # Нельзя складывать строки и числа

# # ZeroDivisionError(Деление на 0)
# number_first = 5
# number_second = 0
#print(number_first_4/ number_second)
# # Делить на 0 нельзя


# # KeyError(Ошибка ключа)
# dictionary = {1: 'Monday', 2: 'Tuesday'}
# print(dictionary[3])
# # Такого ключа не существует


# # # # Name Error(Ошибка имени переменной)
# name = 'Ivan'
# print(names)
# # Переменной names не существует


# # ValueError(Ошибка значения)
# text = 'Python'
# print(int(text))
# # Нельзя символы перевести в целые значения