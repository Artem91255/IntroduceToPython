# #Задайте список из N элементов, заполненных числами из промежутка [-N,N]. 
# # Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число
# # Реализуйте алгоритм перемешивания списка



# import random


# count_of_elements = int(input('Какое количество элементов будет в списке: '))
# elements = []
# for i in range(count_of_elements*2+1):
#     temp_number = count_of_elements * -1
#     elements.append(temp_number)
#     count_of_elements -=1
# print(elements)





# f2 = open('file.txt', 'r')
# l = [line.strip() for line in f2]
# f2.close

# result = [int(item) for item in l]





# #Второй вариант чтения данных из файла и внесением из в список
# # data=[]
# # with open("C:\\Users\\Admin\\Desktop\\GeekBrains\\IntroduceToPython\\Seminars\\file.txt") as f:
# #     for line in f:
# #         data.append([int(x) for x in line.split()])
# # print(data)
# mult = 1
# for i in range(len(result)):
#    x = result[i]
#    mult = mult* elements[x]

# print(mult)


# #Реализуем алгоритм перемешивания списка


# shuffle_elements =elements
# for i in range(len(shuffle_elements)):
#     temp = 0
#     random_number = random.randint(0,len(shuffle_elements)-1)
#     temp = shuffle_elements[i]
#     shuffle_elements[i] = shuffle_elements[random_number]
#     shuffle_elements[random_number] = temp
# print(shuffle_elements)




# # вариант преподавателя
# from random import *

# n = int(input())
# some_list = []
# for _ in range(n):
#     some_list.append(randint(-n,n))
# print(some_list)

# with open('file2.txt', 'w', encoding='utf-8') as f:
#     for _ in range(randint(1, n)):
#         f.write(str(randint(0,n-1)) + '\n')
# fact = 1
# with open('file2.txt', 'r', encoding='utf-8') as f:
#     f = f.read().splitlines()
#     for number in f:
#         fact *=some_list[int(number)]
# print(fact)


# some_list = [1,4,9,10]
# random.shuffle(some_list)

# # реализация shuffle
# for _ in range(random.randint(1,10)):
#     i1= random.randint(0, len(some_list) - 1)
#     i= random.randint(0, len(some_list) - 1)
#     some_list[i1]=some_list[i2] # просто новое присваивание
#     some_list[i1], some_list[i2] = some_list[i2], some_list[i1] # параллельное присваивание. таким образом мы можем менять элементы местами


# реализация с помощью time  
import time
random_number = str(time.time()).split('.')[1]
some_list = [1,4,9,10]

for _ in range(int(str(time.time()).split('.')[1])% (10-5+1)+5):
    i1 = int(str(time.time()).split('.')[1]) % (4-0)+0
    time.sleep(0.00001)
    i2 = int(str(time.time()).split('.')[1]) % (4-0)+0
    some_list[i1], some_list[i2] = some_list[i2], some_list[i1]
print(some_list)










    

