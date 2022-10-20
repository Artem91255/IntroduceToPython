# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму

n = int(input('Задайте размер последовательности: '))
sum = 0
for i in range(1,n+1):
    sum += (1+1/i)**i 
print(round(sum,2))

#вариант от преподавателя

n = int(input())
some_list = []
for i in range(1, n+1):
    some_list.append((1+1/n) **n)
print(sum(some_list))
 