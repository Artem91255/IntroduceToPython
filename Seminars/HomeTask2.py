# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр

a = input('Введите число: ')
sum = 0
for i in range(len(a)):
    if (a[i] == '.' or a[i]==','):
        i+=1
    else:
        temp = int(a[i])
        sum = sum+temp
print(sum)


# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N

b = int(input('Введите число: '))
mult = 1
list=[]
for i in range(1,b+1):
    mult = mult*i
    list.append(mult)
print(list)

# 3. Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму

n = int(input('Задайте размер последовательности: '))
sum = 0
for i in range(1,n+1):
    sum += (1+1/i)**i 
print(round(sum,2))



#4. Задайте список из N элементов, заполненных числами из промежутка [-N,N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число
# Реализуйте алгоритм перемешивания списка
import random


count_of_elements = int(input('Какое количество элементов будет в списке: '))
elements = []
for i in range(count_of_elements*2+1):
    temp_number = count_of_elements * -1
    elements.append(temp_number)
    count_of_elements -=1
print(elements)



f2 = open('C:\\Users\\Admin\\Desktop\\GeekBrains\\IntroduceToPython\\Seminars\\file.txt', 'r')
l = [line.strip() for line in f2]
f2.close

result = [int(item) for item in l]
mult = 1
for i in range(len(result)):
   x = result[i]
   mult = mult* elements[x]

print(mult)


#Реализуем алгоритм перемешивания списка
shuffle_elements =elements
for i in range(len(shuffle_elements)):
    temp = 0
    random_number = random.randint(0,len(shuffle_elements)-1)
    temp = shuffle_elements[i]
    shuffle_elements[i] = shuffle_elements[random_number]
    shuffle_elements[random_number] = temp
print(shuffle_elements)



# 5. ДОП. задача на алгоритмы с реальных собеседований
# Даны два массива:
# [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
# Надо вернуть их пересечение
# [1, 2, 2, 3]
# (порядок не важен)



first_list = [1, 2, 3, 2, 0]
second_list = [5, 1, 2, 7, 3, 2]
third_list = []
for i in range(0, len(first_list)):
    for k in range(0, len(second_list)):
        if first_list[i] == second_list[k]:
            third_list.append(first_list[i])
            k+=1
            break
print(third_list)
