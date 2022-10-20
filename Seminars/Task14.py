# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр

from curses.ascii import isdigit


a = input('Введите число: ')
sum = 0
for i in range(len(a)):
    if (a[i] == '.' or a[i]==','):
        i+=1
    else:
        temp = int(a[i])
        sum = sum+temp
print(sum)

# вариант преподавателя

number = input()
summ = 0
for symbol in number:
    if symbol.isdigit():
        summ+= int(symbol)
print(summ)

