# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


list = [2, 3, 4, 5, 6]
list2 =[]
a = int(len(list)/2)
for i in range(a):
    mult = list[i]*list[len(list)-1-i]
    list2.append(mult)

if len(list)%2!=0:
    list2.append(list[a]**2)
print(list2)