# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 
# и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

number1 = int(input('Введите x: '))
number2 = int(input('Введите y: '))

if number1>0 and number2>0:
    print('1')
elif number1<0 and number2>0:
    print('2')
elif number1<0 and number2<0:
    print('3')
elif number1>0 and number2<0:
    print('4')
else:
    print('Неправильный ввод')