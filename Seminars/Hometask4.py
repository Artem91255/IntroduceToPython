# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# a = float(input('Введите число: '))
# b = input('точность: ')
# print(round(a, len(b.split('.')[1])))

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# b = int(input())
# some_list = []
# a = 2
# while a * a <= b:
#     if b % a == 0:
#         some_list.append(a)
#         b //= a
#     else:
#         a += 1
# if b > 1:
#     some_list.append(b)

# print(some_list)

# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# list=[1,2,3,4,5,5,4,6,8,1]
# list2=[]
# for i in range(len(list)):
#     count=0
#     for j in range(len(list)):
#         if list[i]==list[j]:
#             count+=1
#     if count==1:
#         list2.append(list[i])
        
# print('list2 is: '+str(list2))


# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint
from sympy import symbols
from math import prod

max_value = 100
k = int(input('Введите натуральную степень k:'))

coefficient = [randint(-max_value, max_value) for i in range(k)] + [randint(1, max_value)]
x = symbols('x')

print(sum(map(prod, zip(coefficient, [ x**i for i in range(k + 1)]))), '= 0')

with open('file2.txt','w', encoding='utf-8') as file:
    file.write(str(sum(map(prod, zip(coefficient, [x ** i for i in range(k + 1)])))) + '= 0')