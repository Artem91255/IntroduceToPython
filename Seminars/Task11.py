#Напишите программу, которая принимает на вход число N и выдает последовательность из N членов
import random
a = int(input('Введите число: '))

for i in range(a):
    print(random.uniform(0,100), end= ", ")

#вариант одногруппников: с точки зрения алгоритмической сложности этот вариант лучше

N = int(input('Введите число: '))
for i in range(0,N-1):
    print((-3)**i, end= ', ')
else:
    print((-3)**(N-1))


# Вариант преподавателя

p = int(input('Введите число: '))
for i in range(0,p-1):
    print((-3)**i, end= ', ')
print((-3)**(p-1))

# Второй вариант от преподавателя

q = int(input('Введите число: '))
w = []
for i in range(n):
    w.append((-3) * i)
print(*w, sep=' ')