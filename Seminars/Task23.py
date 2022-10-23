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


# Вариант преподавателя

count = int(input('Tnter count of elements: '))
some_list = []

for _ in range(count):
    number = int(input())
    some_list.append(number)
new_list = []
for idx in range((count-1)//2+1):
    number1 = some_list[idx]
    number2 = some_list[count-idx-1]
    new_list.append(number1*number2)
print(new_list)


