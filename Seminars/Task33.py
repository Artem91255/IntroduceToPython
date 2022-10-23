# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint
from sympy import symbols
from math import prod

max_val = 100
k = int(input('Введите натуральную степень k:'))

koeff = [randint(-max_val, max_val) for i in range(k)] + [randint(1, max_val)]
x = symbols('x')

print(sum(map(prod, zip(koeff, [ x**i for i in range(k + 1)]))), '= 0')

with open('file.txt','w', encoding='utf-8') as file:
    file.write(str(sum(map(prod, zip(koeff, [x ** i for i in range(k + 1)])))) + '= 0')