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
