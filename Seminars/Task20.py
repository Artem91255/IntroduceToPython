# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число
some_list = [18,24,8,12]
some_number = 5
count=0
for i in range(len(some_list)):
    if some_list[i] == some_number:
        count+=1
if count>0:
    print('Присутствует')
else:
    print('Отсутствует')

# teacher
#ищем нужную цифру в списке среди элементов
a = [input() for _ in range(int(input()))]
find_number = input()
if find_number in a:
    print('yes')
else:
    print('no')   
#ищем нужную цифру в самом элементе списка
for i in a:
    if find_number in i:
        print('yess')
        break
else:
    print('noo')



