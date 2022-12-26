# Задача 1: Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# def sum_odd_index(lst):
#     sum = 0
#     for i in range(len(lst)):
#         if i % 2 != 0:
#             sum += lst[i]
#             print(f'On odd positions element: {lst[i]}')
#     print(f'The sum of odd index: {sum}')

# # lst = [2, 3, 5, 9, 3]
# # print(lst)
# # sum_odd_index(lst)

# lst = list(map(int, input('Enter numbers with a space:\n').split()))
# sum_odd_index(lst)

# Задача 2: Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# Вариант 1
# def mult_pairs(lst):
#     accum = len(lst)//2 + 1 if len(lst) % 2 != 0 else len(lst)//2
#     new_lst = [lst[i] * lst[len(lst) - (i + 1)] for i in range(accum)]
#     print(new_lst)

# lst = [2, 3, 4, 5, 6]
# mult_pairs(lst)

# lst = list(map(int, input('Enter numbers with a space:\n').split()))
# mult_pairs(lst)

# Вариант 2

# from math import ceil

# def mult_pairs(array: list[int]) -> list[int]:
#     accum = []
#     for i in range(ceil(len(array) // 2)):
#         accum.append(array[i] * array[-(i + 1)])
#     return accum

# print(mult_pairs([2, 3, 4, 5, 6]))
# print(mult_pairs([2, 3, 5, 6]))

# Задача 3: Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# my_list = list(map(float, input('Enter numbers with a space:\n').split()))
# new_list = [round(i % 1, 2) for i in my_list if i % 1 != 0]
# print(max(new_list) - min(new_list))

# Задача 4: Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# num = int(input('Enter an integer: '))

# result = ''
# while num > 0:
#     result = str(num % 2) + result
#     num //= 2
# print(f'Binary number is: {result}')

# Задача 5:Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

#*Пример:*

#- для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 


def fib(n):
    fib_list = [0]
    x, y = 0, 1
    for i in range(n):
        x, y = y, x + y
        fib_list.append(x)
        fib_list.insert(0, -x if i %2 else x)
    return fib_list

fib_num = int(input('Input number: '))
print(f'For k = {fib_num} the list will look like this: {fib(fib_num)}')


