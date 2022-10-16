# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр

a = input('Введите число: ')
sum = 0
for i in range(len(a)):
    if (a[i] == '.' or a[i]==','):
        i+=1
    else:
        temp = int(a[i])
        sum = sum+temp
print(sum)
