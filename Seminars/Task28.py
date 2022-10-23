
# # Найдите корни квадратного уравнения Ax**2 +Bx + C = 0 двумя спосбами:
# # С помощью математических формул нахождения корней квадратного уравнения
# # С помощью дополнительных библиотек python




# a = int(input('Enter A: '))
# b = int(input('Enter B: '))
# c = int(input('Enter C: '))

# d = b**2 - 4*a*c
# print(d)
# if d<0:
#     print('Корней нет')
# elif d==0:
#     x=0
#     x=-(b/(2*a))
#     print('x = '+str(x))
# else:
#     x1 = 0
#     x2 = 0
#     x1 = (-b+ (d**0.5))/(2*a)
#     x2 = (-b- (d**0.5))/(2*a)
#     print('x1 = '+str(x1))
#     print('x2 = '+str(x2))


# #Вариант одногруппников

# a, b, c = map(int, input().split())
# d = b**2 - 4 * a * c
# if d<0:
#     print('Решений нет')
# elif d==0:
#     print(-b / 2*a)
# else:
#     print((-b + d**0.5) / 2 *  

# #вариант с использованием библиотеки SymPy

# from sympy import *

# a, b, c = map(int, input().split())
# x = Symbol('x')
# print(solve(a*x**2 + b*x + c, x)) # Данный метод решает уравнение. 


# вариант преподавателя
import sympy as sm
a = int(input())
b = int(input())
c = int(input())

d = b ** 2 - 4 * a * c
if d<0:
    print('Действительных корней нет')
elif d == 0:
    print(-b/(2*a))
else:
    print((-b+d ** 0.5) / (2*a), (-b - d **0.5) / (2*a))

x = sm.Symbol('x')
print(sm.solveset(a*x ** 2 + b * x + c, x)) # x =необязательный аргумент после запятой





