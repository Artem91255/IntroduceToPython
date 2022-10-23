# Задайте два числа. Напишите программу, которая найдет НОК(наименьшее общее кратное) этих двух чисел
# если остаток от деления на 2 равен нулю, то счетчик плюс 1. потом находим остаток от деления. и счетчик - это степень двойки
# import math
# a=int(input('Enter first number: '))
# b=int(input('Enter second number: '))
# greater = 0

# if a>b:
#     greater=a
# else:
#     greater=b

# while(True):
#     if (greater%a==0) and(greater%b==0):
#         lcm = greater
#         break
#     greater+=1

# print(lcm)

#     #Второй вариант
# print(math.lcm(a,b))

# #Вариант одногруппников

# a,b = map(int, input().split())
# for i in range(min(a,b), a*b+1, min(a,b)):
#     if i % a ==0 and i%b ==0:
#         print(i)
#         break

    # вариант преподавателя
import sympy as sm

print(sm.lcm(int(input()), int(input())))
