# Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30

#мое решение

number_start = int(input('Введите число: '))

if (number_start%5==0 and number_start%10==0 or number_start%15==0) and not number_start%30==0:
    print('Проверка успешна')
else:
    print('проверка не успешна')

#решение преподавателя

n = int(input('Введите число: '))
if (n%5==0 and n%10==0 or n%15==0) and n%30 !=0:
    print('yes')
else:
    print('no')
