# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


list = [1.1, 1.2, 3.1, 5, 10.01]
list2=[]

for i in range(len(list)):
    x = list[i]
    y= round(x%1,2)
    if y!=0:
        list2.append(y)

min_number = list2[0]
max_number = list2[0]
for i in range(len(list2)):
    if list2[i] < min_number:
        min_number=list2[i]
    if list2[i] > max_number:
        max_number = list2[i]

print(max_number-min_number)


# Вариант преподавателя

count = int(input('Enter count of elements: '))
some_list = []
for _ in range(count):
    number = input()
    some_list.append(number)
minn = 1
maxx = 0
for el in some_list:
    if '.' in str(el):
        dr = str(el).split('.')[1]
        if float('0.' + dr) > maxx:
            maxx = float('0.' + dr)
        elif float('0.' + dr) < minn:
            minn = float('0.' + dr)
print(maxx-minn)
