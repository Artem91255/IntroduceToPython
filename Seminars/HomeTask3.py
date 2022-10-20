# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


list = [2, 3, 5, 9, 3, 1]
summ = 0
for i in range(1,len(list),2):
    summ+=list[i]
print(summ)

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

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


number = int(input('Введите число: '))
#вариант без использования цикла
print(format(number, 'b'))
#Вариант с использованием цикла
y = 0
bin_number = ""
while number>0:
    y=str(number%2)
    bin_number=y+bin_number
    number = int(number/2)
print(bin_number)


# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# числа фибоначчи - первые два числа равны 0 и 1, а каждое последующее число равно сумме двух предыдущих чисел.
# F−n = (−1)**n+1*Fn.
# Fn = F(n+2)−F(n+1).
# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

size = int(input("Задайте размер списка: "))

list1=[]
list2=[]
for i in range(2):
    list1.append(i)
    list2.append(i)
    
temp_number = 0
temp_number2 = 0
for i in range(1,size):
    temp_number = list1[i]+ list1[i-1]
    temp_number2 = list2[i-1] - list2[i]
    list1.append(temp_number)
    list2.append(temp_number2)

list3=[]
for i in range(size,0,-1):
    list3.append(list2[i])
for i in range(size+1):
    list3.append(list1[i])

print(list3)
