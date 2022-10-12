# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
# d = √ [(x2-x1)2+ (y2-y1)2 ] , Где  (x1,y1) и (x2,y2) две точки на плоскости xy
import math


print('Ввод координат для точки А')
x1 = int(input('Введите x: '))
y1 = int(input('Введите y: '))

print('Ввод координат для точки B')
x2 = int(input('Введите x: '))
y2 = int(input('Введите y: '))

d = round(math.sqrt(((x2-x1)**2) + ((y2-y1)**2)),2)
print(d)
